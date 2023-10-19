import os
import json

mode = "python"

levels = input("Levels: ")
levels = int(levels) if levels else 5

with open("data", "w") as f:
    json.dump({"levels": levels, "current_level": 1, "mode": mode}, f)

for i in range(levels):
    os.makedirs(f"level_{i + 1}/files", exist_ok=True)
    os.makedirs(f"level_{i + 1}/out", exist_ok=True)
    if mode == "python":
        with open(f"level_{i + 1}/level_{i + 1}.py", "w") as f, open("level_x.py.template") as t:
            f.write(t.read())
            
    elif mode == "node":
        with open(f"level_{i + 1}/level_{i + 1}.ts", "w") as f, open("level_x.ts.template") as t:
            f.write(t.read())
    
    elif mode == "rust":
        with open(f"level_{i + 1}/level_{i + 1}.rs", "w") as f, open("level_x.rs.template") as t:
            f.write(t.read())
        