"""External evaluation only; upstream code remains unchanged."""
import ast, importlib, json, pathlib, sys, tempfile, traceback
sys.path.insert(0, str(pathlib.Path("upstream/skai/skterminal").resolve()))
import config
report = {"source": "Endrx2008/skai_ap", "commit": "3bd015fe45653b867fab2cb8c98e7c8c8f0a8238", "adaptations": [
"Temporary SKAI_HOME and memory file", "Skip terminal stream wrappers for test import",
"Use qwen2.5:0.5b CPU test model instead of upstream qwen2.5:14b"], "checks": {}}
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    config.SKAI_HOME = root / "home"
    config.MODEL = "qwen2.5:0.5b"
    import memory
    memory.MEMORY_FILE = root / "memory.json"
    source = pathlib.Path("upstream/skai/skterminal/main.py").read_text()
    tree = ast.parse(source)
    tree.body = [n for n in tree.body if not (isinstance(n, ast.Assign) and any(
        isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == "sys"
        and t.attr in ("stdin", "stdout") for t in n.targets))]
    ns = {"__name__": "skai_evaluation", "__file__": str(pathlib.Path("upstream/skai/skterminal/main.py").resolve())}
    exec(compile(tree, "upstream/skai/skterminal/main.py", "exec"), ns)
    def check(name, fn):
        try: report["checks"][name] = fn()
        except Exception as exc: report["checks"][name] = {"error": str(exc)}
    check("create_read", lambda: {"create": ns["dispatch_tool"]("create_file", {"filename":"notes.txt","content":"hello"}),
        "read": ns["dispatch_tool"]("read_file", {"filename":"notes.txt"})})
    def memcheck():
        m = memory.load_memory()
        m["user"]["name"] = "Test User"
        memory.save_memory(m)
        return {"roundtrip": memory.load_memory()["user"]["name"] == "Test User"}
    check("memory", memcheck)
    def absolute_probe():
        target = root / "outside.txt"
        value = ns["dispatch_tool"]("create_file", {"filename": str(target), "content":"temporary boundary probe"})
        return {"escaped_workspace": target.exists(), "result": value}
    check("absolute_path_boundary", absolute_probe)
    def plain():
        answer = ns["ask_ollama"]([{"role":"user","content":"Reply with exactly SKAI_RUNNER_OK"}], temperature=0, max_tokens=32)
        return {"answer":answer,"exact_match":answer=="SKAI_RUNNER_OK"}
    check("live_local_inference", plain)
    def model_tool():
        answer = ns["ask_ollama"]([{"role":"system","content":config.CHAT_SYSTEM},
            {"role":"user","content":"Create runner-note.txt containing Hello from Skai. Return the tool JSON only."}], temperature=0, max_tokens=200)
        calls = ns["parse_tool_calls"](answer)
        results=[]
        for call in calls or []:
            params=call.get("params",{})
            if call["tool"]=="create_file" and isinstance(params,dict) and params.get("filename")=="runner-note.txt":
                results.append(ns["dispatch_tool"]("create_file",params))
            else: results.append("Blocked by evaluation allowlist")
        return {"answer":answer,"parsed":calls,"results":results,
            "file_created":(config.SKAI_HOME/"runner-note.txt").exists()}
    check("model_to_tool", model_tool)
    report["limits"]=["No upstream default 14B/GPU qualification", "No live web search or browser-extension execution",
        "Path boundary findings are diagnostic; do not grant broad filesystem access"]
pathlib.Path("evidence").mkdir(exist_ok=True)
pathlib.Path("evidence/skai-report.json").write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if report["checks"].get("live_local_inference",{}).get("answer","ERROR").startswith("ERROR"):
    raise SystemExit(1)
