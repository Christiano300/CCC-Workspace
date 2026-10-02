from io import TextIOWrapper
import numpy as np

def solve(file: TextIOWrapper, out: TextIOWrapper):
    lines = iter(file.readlines())
    count = int(next(lines).strip())
    for _ in range(count):
        limits = next(lines).strip().split(" ")
        height = int(limits[1])
        limit = int(limits[2])
        grid = []
        for _ in range(height + 2):
            line = next(lines).strip()
            grid.append(list(line))
        next(lines)
        
        if len(grid) == 5:
            for i in range(1, len(grid[0]) - 1):
                grid[2][i] = "X"
            idx = grid[0].index("S")
            grid[1][idx] = "X"
        
        elif len(grid[0]) == 5:
            for i in range(1, len(grid) - 1):
                grid[i][2] = "X"
            idx = grid[0].index("S")
            grid[1][idx] = "X"
        
        out.write("".join("".join(row) + "\n" for row in grid) + "\n")
            
        
        
    

with open("level_3/files/level3_1_small.in") as f, open("level_3/out/level_3_1_small.out", "w") as out:
    solve(f, out)

with open("level_3/files/level3_2_large.in") as f, open("level_3/out/level_3_2_large.out", "w") as out:
    solve(f, out)


