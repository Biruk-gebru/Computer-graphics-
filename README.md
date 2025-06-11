# Tic-Tac-Toe Game

## Introduction
This is a classic Tic-Tac-Toe game implemented using Pygame and OpenGL. It features both a single-player mode against an AI and a two-player mode.

## Features
*   **Single Player Mode**: Play against an intelligent AI.
*   **Two Player Mode**: Play against another human player.
*   **Interactive Game Board**: Graphical representation of the Tic-Tac-Toe board.
*   **Restart Option**: Easily restart the game after it ends.

## How to Play
1.  **Run the game**: Execute the `Assignment.py` file.
2.  **Choose Game Mode**: A selection screen will appear. Click "Single Player" to play against the AI, or "Two Player" to play with another person.
3.  **Making Moves**: Click on an empty cell on the game board to place your mark.
    *   In Single Player mode, you are "X", and the AI is "O".
    *   In Two Player mode, players alternate turns, with "X" starting first.
4.  **Winning/Drawing**: The game ends when a player gets three of their marks in a row (horizontally, vertically, or diagonally), or when all cells are filled resulting in a draw.
5.  **Restart**: After a game concludes, a prompt will appear asking if you wish to play again.

## Game Logic

### Overview
The game manages its state using a 3x3 board represented by a list of lists. Each cell can be `None` (empty), 'X', or 'O'. Player turns alternate, and the game checks for win or draw conditions after each move.

### Winning Conditions
The `check_winner(board)` function determines if there's a winner by checking all possible winning lines:
*   Three horizontal rows.
*   Three vertical columns.
*   Two diagonal lines.
If a player's mark occupies all three cells in any of these lines, that player is declared the winner.

### Draw Conditions
The `is_draw(board)` function checks if all cells on the board are filled (`is not None`) and no winner has been declared. If both conditions are true, the game is a draw.

## AI Algorithm: Minimax

### How Minimax Works
The AI in the single-player mode uses the **Minimax algorithm** to determine its best move. Minimax is a decision-making algorithm used in game theory for optimal play in two-player zero-sum games (like Tic-Tac-Toe). It works by exhaustively searching the game tree, evaluating all possible future moves to a certain depth (in Tic-Tac-Toe, it can search to the end of the game).

*   **Maximizing Player (AI - 'O')**: The AI aims to maximize its score (winning).
*   **Minimizing Player (Opponent - 'X')**: The AI assumes the opponent will play optimally to minimize the AI's score (prevent the AI from winning).

### `minimax(board, is_maximizing)` function
This recursive function forms the core of the AI. It takes the current `board` state and a boolean `is_maximizing` (true if it's the AI's turn, false if it's the player's turn). It returns a score:
*   `1`: If AI ('O') wins.
*   `-1`: If Player ('X') wins.
*   `0`: If it's a draw.

The function explores all possible moves from the current state, and for each move, it recursively calls itself to evaluate the outcome assuming optimal play from both sides.

### `best_move(board)` function
This function iterates through all empty cells on the current `board`. For each empty cell, it temporarily places the AI's mark ('O'), calls `minimax` to evaluate the score of that move, and then undoes the move. It keeps track of the move that yields the highest score (best outcome for the AI) and returns that move.

## Flowchart
```mermaid
graph TD
    A[Start Game] --> B{Choose Mode?}
    B -- Single Player --> C[Initialize Board for AI (O) vs Player (X)]
    B -- Two Player --> D[Initialize Board for Player X vs Player O]

    C --> E[Game Loop]
    D --> E

    E --> F{Player X's Turn?}
    F -- Yes --> G[Wait for Player X's Mouse Click]
    F -- No (AI's turn or Player O's turn) --> H{Is it AI's Turn (Single Player)?}

    G --> I[Validate Move & Update Board]
    I --> J{Check Winner?}
    J --> K{Check Draw?}

    H -- Yes --> L[Calculate Best Move using Minimax]
    L --> I
    H -- No --> G

    K -- No --> F
    K -- Yes --> M{Game Over?}

    J -- No --> K
    J -- Yes --> M

    M -- Yes --> N[Display Result]
    N --> O{Play Again?}
    O -- Yes --> A
    O -- No --> P[End Game]
```

## Setup and Run

### Prerequisites
*   Python 3.x
*   Pygame library
*   PyOpenGL library

### Installation
1.  **Install Python**: If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
2.  **Install Pygame**: Open your terminal or command prompt and run:
    ```bash
    pip install pygame
    ```
3.  **Install PyOpenGL**: Open your terminal or command prompt and run:
    ```bash
    pip install PyOpenGL PyOpenGL_accelerate
    ```

### Running the Game
1.  Navigate to the directory where `Assignment.py` is located.
2.  Run the script using Python:
    ```bash
    python Assignment.py
    ``` 