import random
import string

# Create the Game Grid
def create_grid(size):
    # Initialize the grid with 'O' (ocean) in all cells
    grid = [['O' for _ in range(size)] for _ in range(size)]
    return grid

# Display the Grid
def print_grid(grid):
    # Display the grid with row numbers and column letters
    print("   " + " ".join(string.ascii_uppercase[:len(grid)]))
    for i, row in enumerate(grid):
        print(f"{i+1:2} " + " ".join(row))

# Place Computer's Battleships
def place_ships(grid, num_ships):
    # Randomly place computer's battleships on the grid
    for _ in range(num_ships):
        while True:
            ship_row = random.randint(0, len(grid) - 1)
            ship_col = random.randint(0, len(grid) - 1)
            if grid[ship_row][ship_col] == 'O':
                grid[ship_row][ship_col] = 'S'
                break

# Check Valid Guess
def is_valid_guess(guess, size):
    # Check if the player's guess is within the grid boundaries
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
        if len(guess) != 2 or not guess[1].isdigit():
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
            player_grid[row][col] = 'H'  # 'H' represents a hit on a battleship
            computer_grid[row][col] = 'X' 
        else:
            print("You missed.")
            player_grid[row][col] = 'X' # 'X' represents a missed shot


        print("Your grid:")
        print_grid(player_grid)

        if 'S' not in [cell for row in computer_grid for cell in row]:
            print("Congratulations! You sank all the battleships. You win!")
            break

        turns += 1

if __name__ == "__main__":
    grid_size = int(input("Enter the grid size (e.g., 6): "))
    num_ships = int(input("Enter the number of battleships (e.g., 4): "))
    play_battleships(grid_size, num_ships)
