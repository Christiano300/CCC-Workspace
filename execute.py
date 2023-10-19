from io import StringIO
import os
import shutil

def execute(mode: str, current_level: int, is_example: bool) -> str:
    if mode == "python":
        level = __import__(f"level_{current_level}.level_{current_level}").__dict__[f"level_{current_level}"]
        out = StringIO()
        with open(f"level_{current_level}/files/level{current_level}{'_example' if is_example else ''}.in") as f:
            level.solve(f, out)
        out.flush()
        return out.getvalue()
    
    elif mode == "node":
        os.system("tsc level_1/level_1.ts --esModuleInterop true")
        import json
        with open("package.json", "r") as f:
            package = json.load(f)
            package["main"] = f"level_{current_level}/level_{current_level}.js"
        with open("package.json", "w") as f:
            json.dump(package, f)
        os.system(f"node . level_{current_level}/files/level{current_level}{'_example' if is_example else ''}.in out")
        with open("out") as f:
            text = f.read()
        os.remove("out")
        return text

    elif mode == "rust":
        shutil.copy(f"level_{current_level}/level_{current_level}.rs", "src/main.rs")
        os.system(f"cargo run -- level_{current_level}/files/level{current_level}{'_example' if is_example else ''}.in' out")
        os.remove("src/main.rs")
        with open("src/out") as f:
            text = f.read()
        os.remove("src/out")
        return text
        

    raise Exception("Invalid mode: " + mode)