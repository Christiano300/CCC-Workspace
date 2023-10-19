import json
import os

from execute import execute

with open("data", "r") as f:
    data = json.load(f)

current_level = data["current_level"]


files = os.listdir(f"level_{current_level}/files")
for i, file in enumerate(files):
    if "example" in file:
        continue
    with open(
        f"level_{current_level}/out/level{current_level}_{i + 1}.out", "w"
    ) as f_out:
        out = execute(data["mode"], current_level, False)
        f_out.write(out)

print("Terminal offenlassen!")
advance = input("Hats funktioniert? [Y/n] ") in ["", "y", "Y"]
if advance:
    data["current_level"] += 1
    with open("data", "w") as f:
        json.dump(data, f)
