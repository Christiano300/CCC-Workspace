from io import TextIOWrapper
import numpy as np

def apply_height_pattern(grid):
    # returns a new grid (deep copy) with the "height % 3 == 0" pattern applied
    new = [row[:] for row in grid]
    for i in range(1, len(new) - 1):
        new[i][2] = "X"
    idx = new[0].index("S")
    new[1][idx] = "X"
    for i in range(2, len(new) - 1, 3):
        for j in range(3, len(new[0]) - 1):
            new[i][j] = "X"
    return new

def apply_width_pattern(grid):
    # returns a new grid (deep copy) with the "width % 3 == 0" pattern applied
    new = [row[:] for row in grid]
    idx = new[0].index("S")
    new[1][idx] = "X"
    for i in range(1, len(new[0]) - 1):
        new[len(new) - 3][i] = "X"
    for i in range(2, len(new[0]) - 1, 3):
        for j in range(1, len(new) - 2):
            new[j][i] = "X"
    return new

def solve(file: TextIOWrapper, out: TextIOWrapper):
    lines = iter(file.readlines())
    count = int(next(lines).strip())
    for _ in range(count):
        limits = next(lines).strip().split(" ")
        width = int(limits[0])
        height = int(limits[1])
        limit = int(limits[2])
        grid = []
        for _ in range(height + 2):
            line = next(lines).strip()
            grid.append(list(line))
        next(lines)
        
        if width == 3:
            for i in range(1, len(grid) - 1):
                grid[i][2] = "X"
            idx = grid[0].index("S")
            grid[1][idx] = "X"
        
        elif height == 3:
            for i in range(1, len(grid[0]) - 1):
                grid[2][i] = "X"
            idx = grid[0].index("S")
            grid[1][idx] = "X"
        
        
        else:
            
            # try height pattern first
            h_grid = apply_height_pattern(grid)
            h_count = sum(row.count("X") for row in h_grid)
            if h_count <= limit:
                grid = h_grid
            else:
                # try width pattern
                w_grid = apply_width_pattern(grid)
                w_count = sum(row.count("X") for row in w_grid)
                if w_count <= limit:
                    grid = w_grid
                else:
                    print("Exceeded limit for both patterns:", h_count, w_count, ">", limit)    
        
        fff = "".join("".join(row) + "\n" for row in grid) + "\n"
        out.write(fff)
        if fff.count("X") > limit:
            print("Exceeded limit:", fff.count("X"), ">", limit)
            
        
        
    

with open("level_4/files/level4_1_small.in") as f, open("level_4/out/level_4_1_small.out", "w") as out:
    solve(f, out)

with open("level_4/files/level4_2_large.in") as f, open("level_4/out/level_4_2_large.out", "w") as out:
    solve(f, out)


