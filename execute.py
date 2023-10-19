from io import StringIO
import os
import shutil

def execute(mode: str, current_level: int, is_example: bool, test_num: int = 0) -> str:
    if mode == "python":
        level = __import__(f"level_{current_level}.level_{current_level}").__dict__[f"level_{current_level}"]
        out = StringIO()
        with open(f"level_{current_level}/files/level{current_level}{'_example' if is_example else '_' + str(test_num)}.in") as f:
            level.solve(f, out)
        out.flush()
        return out.getvalue()
    
    elif mode == "node":
        import json
        with open("data", "r") as f:
            data = json.load(f)
        if not data.get("compiled"):
            os.system("tsc level_1/level_1.ts --esModuleInterop true")

        data["compiled"] = True
        with open("data", "w") as f:
            json.dump(data, f)
        
        import json
        with open("package.json", "r") as f:
            package = json.load(f)
            package["main"] = f"level_{current_level}/level_{current_level}.js"
        with open("package.json", "w") as f:
            json.dump(package, f)
        os.system(f"node . level_{current_level}/files/level{current_level}{'_example' if is_example else '_' + str(test_num)}.in out.txt")
        with open("out.txt") as f:
            text = f.read()
        os.remove("out.txt")
        return text

    elif mode == "rust":
        shutil.copy(f"level_{current_level}/level_{current_level}.rs", "src/main.rs")
        os.system(f"cargo run -- ../level_{current_level}/files/level{current_level}{'_example' if is_example else test_num}.in' out.txt")
        with open("out.txt") as f:
            text = f.read()
        return text
        

    raise Exception("Invalid mode: " + mode)