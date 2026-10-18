"""Runner-side guard for the external Skai dispatcher, not an upstream modification.
GPL-3.0-or-later: intended for use alongside Endrx2008/skai_ap.
This guard does not defend against concurrent symlink swaps by another process.
"""
from pathlib import Path
PATH_KEYS = {"filename","file","name","path","old","new","old_name","new_name","dirname",
"foldername","folder","destination","dest","destination_folder","source","source_filename",
"old_file","old_filename","new_file","new_filename"}
BULK = {"delete_all","rm_all","delete_all_files","clear_folder","clear"}
def checked_path(root, value):
    if not isinstance(value,str) or not value.strip():
        raise ValueError("Path must be a nonempty string")
    p=Path(value)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("Absolute paths and parent traversal are refused")
    base=Path(root).resolve()
    resolved=(base/p).resolve()
    if resolved == base or not resolved.is_relative_to(base):
        raise ValueError("Path must stay inside the working folder")
    return resolved
def guarded_dispatch(dispatch,root):
    def call(tool,params):
        if not isinstance(params,dict): return "Error: tool parameters must be an object"
        if tool in BULK or any(params.get(k) for k in ("all","all_files","directory")):
            return "Error: bulk deletion is disabled in the external evaluation adapter"
        try:
            for k,v in params.items():
                if k in PATH_KEYS: checked_path(root,v)
                if k=="files":
                    if not isinstance(v,list):raise ValueError("files must be a list")
                    for item in v:checked_path(root,item)
        except (ValueError,TypeError,OSError) as exc:
            return "Error: " + str(exc)
        return dispatch(tool,params)
    return call
def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base=Path(tmp)/"home";base.mkdir()
        outside=Path(tmp)/"outside";outside.mkdir()
        (base/"link").symlink_to(outside,target_is_directory=True)
        for bad in (str(outside/"x"),"../outside/x","link/x","."):
            try:checked_path(base,bad)
            except ValueError:pass
            else:raise AssertionError("Accepted boundary escape: "+bad)
        assert checked_path(base,"nested/note.txt")==base/"nested/note.txt"
        invoked=[]
        call=guarded_dispatch(lambda t,p:invoked.append((t,p)) or "ok",base)
        assert call("create_file",{"filename":"../outside.txt"}).startswith("Error:")
        assert not invoked
        assert call("create_file",{"filename":"note.txt","content":"hello"})=="ok"
        assert len(invoked)==1
if __name__=="__main__":
    self_test()
    print("Guard regressions passed: absolute, traversal, symlink, root, allowed nested path, dispatcher gating")
