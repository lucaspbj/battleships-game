import random
import string

def create_grid(size):
    """
    Create a grid with a specified size.

    Args:
    size (int): The size of the grid.

    Returns:
    list: A 2D list representing the grid.
    """
    grid = [['O' for _ in range(size)] for _ in range(size)]
    return grid

def print_grid(grid):
    """
    Display the game grid with computer's ships hidden.

    Args:
    grid (list): The 2D list representing the game grid.
    """
    visible_grid = [['O' if cell == 'S' else cell for cell in row] for row in grid]
    print("   " + " ".join(string.ascii_uppercase[:len(grid)]))
    for i, row in enumerate(visible_grid):
        print(f"{i+1:2} " + " ".join(row))

def place_ships(grid, num_ships):
    """
    Place computer's battleships on the grid.

    Args:
    grid (list): The 2D list representing the game grid.
    num_ships (int): The number of battleships to place.
    """
    for _ in range(num_ships):
        while True:
            ship_row = random.randint(0, len(grid) - 1)
            ship_col = random.randint(0, len(grid) - 1)
            if grid[ship_row][ship_col] == 'O':
                grid[ship_row][ship_col] = 'S'
                break

def is_valid_guess(guess, size):
    """
    Check if a player's guess is within the grid boundaries.

    Args:
    guess (tuple): A tuple representing the (row, col) guess.
    size (int): The size of the grid.

    Returns:
    bool: True if the guess is valid, False otherwise.
    """
    row, col = guess
    return 0 <= row < size and 0 <= col < size

def play_battleships(size, num_ships):
    """
    Play the Battleships game against the computer.

    Args:
    size (int): The size of the grid.
    num_ships (int): The number of battleships to place.
    """
    grid = create_grid(size)
    computer_grid = create_grid(size)  # Separate grid to track computer's ships

    print("Welcome to Battleships!")
    print("Here is your grid:")
    print_grid(grid)

    place_ships(computer_grid, num_ships)

    turns = 0
    while True:
        print(f"Turn {turns + 1}")
        guess = input("Enter your guess (e.g., A3): ")
        if len(guess) != 2 or not guess[1].isdigit():
            print("Invalid input. Please enter your guess as a letter and a number (e.g., A3).")
            continue
        col = string.ascii_uppercase.index(guess[0].upper())
        row = int(guess[1]) - 1

        if not is_valid_guess((row, col), size):
            print("Your guess is off-grid. Try again.")
            continue

        if grid[row][col] == 'X':
            print("You've already guessed this location. Try again.")
            continue

        if computer_grid[row][col] == 'S':
            print("You hit a battleship!")
            grid[row][col] = 'H'  # 'H' represents a hit on a battleship
            computer_grid[row][col] = 'X' 
        else:
            print("You missed.")
            grid[row][col] = 'X' # 'X' represents a missed shot

        print("Your grid:")
        print_grid(grid)

        if 'S' not in [cell for row in computer_grid for cell in row]:
            print("Congratulations! You sank all the battleships. You win!")
            break

        turns += 1

if __name__ == "__main__":
    grid_size = int(input("Enter the grid size (e.g., 6): "))
    num_ships = int(input("Enter the number of battleships (e.g., 4): "))
    play_battleships(grid_size, num_ships)