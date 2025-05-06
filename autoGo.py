import subprocess

def run_script(script_name):
    print(f"running {script_name}...")
    subprocess.run(["python3", script_name])

# Execute each program file sequentially
if __name__ == "__main__":
    scripts = ["13CCSPs.py", "pkm2std.py", "mergepk.py", "final.py", "edge.py"]
    for script in scripts:
        run_script(script)
