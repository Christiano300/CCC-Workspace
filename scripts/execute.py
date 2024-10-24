import importlib
from io import StringIO
import os
import shutil
import sys

def execute(mode: str, current_level: int, is_example: bool, test_num: int = 0) -> str:
    if mode == "python":
        levelpath = f"level_{current_level}"
        sys.path.append(f"{levelpath}")
        level = importlib.import_module(f"{levelpath}")
        out = StringIO()
        with open(f"level_{current_level}/files/level{current_level}{'_example' if is_example else '_' + str(test_num)}.in") as f:
            level.solve(f, out)
        out.flush()
        return out.getvalue()

    elif mode == "rust":
        shutil.copy(f"../level_{current_level}/level_{current_level}.rs", "src/main.rs")
        os.system(f"cargo run -- ../../level_{current_level}/files/level{current_level}{'_example' if is_example else test_num}.in' out.txt")
        with open("out.txt") as f:
            text = f.read()
        return text


    raise Exception("Invalid mode: " + mode)