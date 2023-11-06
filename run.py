import random
import string

# Create the Game Grid
def create_grid(size):
    grid = [['O' for _ in range(size)] for _ in range(size)]
    return grid

# Display the Grid
def print_grid(grid):
    print("   " + " ".join(string.ascii_uppercase[:len(grid)]))
    for i, row in enumerate(grid):
        print(f"{i+1:2} " + " ".join(row))

# Place Computer's Battleships
def place_ships(grid, num_ships):
    for _ in range(num_ships):
        while True:
            ship_row = random.randint(0, len(grid) - 1)
            ship_col = random.randint(0, len(grid) - 1)
            if grid[ship_row][ship_col] == 'O':
                grid[ship_row][ship_col] = 'S'
                break

#  Check Valid Guess
def is_valid_guess(guess, size):
    row, col = guess
    return 0 <= row < size and 0 <= col < size

# Play the Game
def play_battleships(size, num_ships):
    player_grid = create_grid(size)
    computer_grid = create_grid(size)

    print("Welcome to Battleships!")
    print("Here is your grid:")
    print_grid(player_grid)

    place_ships(computer_grid, num_ships)

    turns = 0
    while True:
        print(f"Turn {turns + 1}")
        guess = input("Enter your guess (e.g., A3): ")
        if len(guess) != 2 or not guess[0].isdigit():
            print("Invalid input. Please enter your guess as a letter and a number (e.g., A3).")
            continue
        col = string.ascii_uppercase.index(guess[0].upper())
        row = int(guess[1]) - 1

        if not is_valid_guess((row, col), size):
            print("Your guess is off-grid. Try again.")
            continue

        if player_grid[row][col] == 'X':
            print("You've already guessed this location. Try again.")
            continue

        if computer_grid[row][col] == 'S':
            print("You hit a battleship!")
            computer_grid[row][col] = 'X'
        else:
            print("You missed.")
            player_grid[row][col] = 'X'

        print("Your grid:")
        print_grid(player_grid)

        if all(all(cell == 'X' for cell in row) for row in computer_grid):
            print("Congratulations! You sank all the battleships. You win!")
            break