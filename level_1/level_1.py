from io import TextIOWrapper
import numpy as np

def solve(file: TextIOWrapper, out: TextIOWrapper):
    lines = iter(file.readlines())
    lines.__next__()
    for line in lines:
        parts = list(map(int, line.strip().split()))
        arr = [["#" for _ in range(parts[0] + 2)] for _ in range(parts[1] + 2)]
        for i in range(1, parts[1] + 1):
            for j in range(1, parts[0] + 1):
                arr[i][j] = ":"
    
        out.write("".join("".join(row) + "\n" for row in arr) + "\n")
        
    
    
    out.write("")