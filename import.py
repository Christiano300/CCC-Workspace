import json
import os
import zipfile

with open("data", "r") as f:
    data = json.load(f)

current_level = data["current_level"]

if not os.path.exists(f"level{current_level}.zip"):
    print(f"level{current_level}.zip nicht gefunden!")
    quit()

with zipfile.ZipFile(f"level{current_level}.zip", "r") as zip_ref:
    zip_ref.extractall(f"level_{current_level}/files")