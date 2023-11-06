import random
import string

def create_grid(size):
    grid = [['O' for _ in range(size)] for _ in range(size)]
    return grid

def print_grid(grid):
    print("   " + " ".join(string.ascii_uppercase[:len(grid)]))
    for i, row in enumerate(grid):
        print(f"{i + 1:2} " + " ".join(row))
