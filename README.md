# Battleships Game

This is a simple implementation of the classic game "Battleships" in Python, where you play against the computer.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Contributing](#contributing)

## Description

This Python program allows you to play the classic game of Battleships against the computer. It provides a text-based grid where you can guess the location of the computer's hidden battleships.

## Features

- A grid is displayed to represent your game board.
- Battleships are hidden on the computer's game board.
- You can guess the locations of the computer's battleships.
- The game continues until you sink all the computer's battleships or you give up.
- The game provides feedback on each guess, indicating whether you hit or missed a battleship.

## Getting Started

To play the game, follow these steps:

1. Clone the repository to your local machine.

2. Run the game by executing the `run.py` script.

3. Follow the on-screen instructions to set the grid size and the number of battleships.

4. Start guessing the locations of the computer's battleships.

## How to Play

- The grid will be displayed with letters representing columns and numbers representing rows.
- Enter your guess in the format of a letter and a number (e.g., A3) when prompted.
- The game will provide feedback on each guess.
- Keep guessing until you sink all the computer's battleships or decide to give up.

## Known Issues and Limitations

- **Grid Size Limitation:** The game currently has a limitation where if you enter a grid size larger than 9, it may not function as expected. This is a known bug, and I am working to address it in future releases.

- **Guess Hit Display:** When a player enters a guess that was previously chosen and it's a hit, the display may change to 'X' instead of maintaining the 'H' for a hit. This is another known issue that I plan to resolve in the future.

Please feel free to report any issues you encounter or provide feedback to help us improve the game. We appreciate your input and support in making this project better.

## To-Do List

- [ ] Fix input validation for grid size > 9
- [ ] Preserve 'H' for hit instead of changing to 'X' on repeated guesses
- [ ] Other improvements...

Please feel free to contribute to the project by working on these tasks.

## Contributing

Contributions are welcome! If you want to improve the game or fix any issues, please create a pull request.

Enjoy playing the Battleships game!
