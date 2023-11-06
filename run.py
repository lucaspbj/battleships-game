import random
import string

def create_grid(size):
    grid = [['O' for _ in range(size)] for _ in range(size)]
    return grid

def print_grid(grid):
    print("   " + " ".join(string.ascii_uppercase[:len(grid)]))
    for i, row in enumerate(grid):
        print(f"{i + 1:2} " + " ".join(row))

def place_ships(grid, num_ships):
    for _ in range(num_ships):
        while True:
            ship_row = random.randint(0, len(grid) - 1)
            ship_col = random.randint(0, len(grid) - 1)
            if grid[ship_row][ship_col] == 'O':
                grid[ship_row][ship_col] = 'S'
                break

def is_valid_guess(guess, size):
    row, col = guess
    return 0 <= row < size and 0 <= col < size
