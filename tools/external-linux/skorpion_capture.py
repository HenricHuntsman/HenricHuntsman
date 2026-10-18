import pathlib, shutil, socket, subprocess, time
out=pathlib.Path("evidence");out.mkdir(exist_ok=True)
shutil.copy("/usr/share/OVMF/OVMF_VARS_4M.fd","/tmp/skorpion-vars.fd")
cmd=["qemu-system-x86_64","-machine","q35","-accel","tcg","-m","2048","-smp","2",
"-drive","if=pflash,format=raw,readonly=on,file=/usr/share/OVMF/OVMF_CODE_4M.fd",
"-drive","if=pflash,format=raw,file=/tmp/skorpion-vars.fd",
"-cdrom","skorpion.iso","-boot","d","-snapshot","-nic","none","-display","none",
"-monitor","unix:/tmp/skorpion-monitor,server=on,wait=off",
"-serial","file:evidence/serial.log","-no-reboot"]
log=open(out/"qemu.log","wb")
p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT)
try:
    for _ in range(100):
        if pathlib.Path("/tmp/skorpion-monitor").exists():break
        if p.poll() is not None:raise RuntimeError("QEMU startup failed")
        time.sleep(.1)
    with socket.socket(socket.AF_UNIX) as s:
        s.settimeout(5);s.connect("/tmp/skorpion-monitor");s.recv(4096)
        for sec in (30,60,90,120):
            time.sleep(30)
            if p.poll() is not None:raise RuntimeError("QEMU exited")
            target=(out/f"skorpion-{sec}s.ppm").resolve()
            s.sendall(f"screendump {target}\n".encode())
            for _ in range(100):
                if target.exists() and target.stat().st_size>100:break
                time.sleep(.1)
            if not target.exists():raise RuntimeError("Missing screenshot")
            s.recv(65536)
    (out/"LIMITS.txt").write_text("Captured displays require visual review. No boot or installation success is inferred from job success. Guest networking disabled; no host disk attached. ISO came from upstream README link; locally computed digest records bytes but is not publisher authentication.")
finally:
    p.terminate()
    try:p.wait(timeout=10)
    except subprocess.TimeoutExpired:p.kill();p.wait()
    log.close()
