import json
from execute import execute

with open("data", "r") as f:
    data = json.load(f)

current_level = data["current_level"]

with open(f"level_{current_level}/files/level{current_level}_example.out") as correct:
    correct = correct.read()
    out = execute(data["mode"], current_level, True)
    if correct == out:
        print("\033[92;1mTestfall erfolgreich\033[0m")
    else:
        print("\033[31;1mTestfall fehlgeschlagen\033[0m")
        print("Erwartet: ")
        print(correct)
        print("\n\nErhalten: ")
        print(out)
        quit()