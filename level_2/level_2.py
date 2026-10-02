from io import TextIOWrapper
import numpy as np

def solve(file: TextIOWrapper, out: TextIOWrapper):
    for line in file.readlines():
        if line.startswith("#"):
            if line[1] == ":":
                out.write("#:X:#" + "\n")
            else:
                out.write(line)
        elif line.strip() == "":
            out.write("\n")

with open("level_2/files/level2_2_large.in") as f, open("level_2/out/level_2_2_large.out", "w") as out:
    solve(f, out)


