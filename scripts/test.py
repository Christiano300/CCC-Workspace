import json
from execute import execute
import os

with open("data", "r") as f:
    data = json.load(f)

current_level = data["current_level"]
if data["mode"] == "node":
    data["compiled"] = False
    with open("data", "w") as f:
        json.dump(data, f)

correct_path = f"level_{current_level}/files/level{current_level}_example.out"
attempt_path = f"level_{current_level}/files/level{current_level}_example_run.out"

with open(correct_path) as correct, \
    open(attempt_path, "w") as attempt_out:
    correct = correct.read()
    out = execute(data["mode"], current_level, True)
    if correct == out:
        print("\033[92;1mTestfall erfolgreich\033[0m")
    else:
        attempt_out.write(out)
        attempt_out.flush()
        print("\033[31;1mTestfall fehlgeschlagen\033[0m")
        os.system(f"code -r --diff {correct_path} {attempt_path}")