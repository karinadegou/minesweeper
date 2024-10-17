# Minesweeper Game

This is a simple Minesweeper game implemented using Python and `tkinter` for the graphical user interface. The game follows the classic Minesweeper rules: players reveal cells on the grid, and the goal is to flag all the mines without clicking on them.

## Features

- Left-click to reveal a cell.
- Right-click to flag/unflag a cell as a mine.
- Automatically reveals adjacent empty cells when an empty cell is clicked.
- The game ends when the player hits a mine or flags all the mines correctly.
- Simple graphical interface using `tkinter`.

## Requirements

- Python 3.12
- `tkinter` (it comes pre-installed with most Python distributions)

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/karinadegou/minesweeper.git
    cd minesweeper
    ```

2. Run the game:

    ```bash
    python main.py
    ```

## Gameplay

- **Left-click** on a cell to reveal it.
- **Right-click** on a cell to flag/unflag it as a mine.
- If you reveal a mine, the game is over.
- If you flag all mines correctly, you win the game.
