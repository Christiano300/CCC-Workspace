import sys

if len(sys.argv <= 1):
    print("Print help message here")
    exit()

binaries = ["python3.exe", "python.exe"]
for bin in binaries:
    on_path = os.run(f"where {bin}", capture_output=True, text=True).split("\n")
    for path in on_path:
        if resolve_symlink(path.strip()).endswith("AppInstallerPythonRedirector.exe"):
            continue 
        if exists(path.strip()):
            run(f'"{path.strip()}" scripts\\ccc.py ' + " ".join(sys.argv[1:]))
            exit()

if exists("%localappdata%\\Python\\bin\\python.exe"):
    run("%localappdata%\\Python\\bin\\python.exe scripts\\ccc.py " + " ".join(sys.argv[1:]))
    exit()

local_installations = os.listdir("%localappdata%\\Programs\\Python")
for installation in local_installations:
    if exists(f"%localappdata%\\Programs\\Python\\{installation}\\python.exe"):
        run(f"%localappdata%\\Programs\\Python\\{installation}\\python.exe scripts\\ccc.py " + " ".join(sys.argv[1:]))
        exit()