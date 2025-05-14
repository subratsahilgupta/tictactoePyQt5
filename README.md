```markdown
# 🎮 PyQt5 Tic Tac Toe – A GUI-Based Two-Player Game

A fully interactive **Tic Tac Toe** (X-O) game developed using **Python** and **PyQt5**. The application offers a simple yet effective GUI built with **Qt Designer (.ui file)** and handles all game logic programmatically. It's ideal for beginners learning GUI programming or classic game logic with Python.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [UI Details](#ui-details)
- [Game Logic](#game-logic)
- [Code Overview](#code-overview)
- [Future Improvements](#future-improvements)
---

## 🧠 Overview

This project demonstrates how to integrate PyQt5's UI capabilities with Python's logical control to create a classic board game. The interface includes:

- A 3x3 grid of buttons representing the game board.
- A dynamic label to show the current turn or game status.
- A reset button to restart the game at any time.

It automatically handles:
- Player turns
- Win condition checks
- Draw state detection
- Game reset behavior

---

## ✅ Features

- 👥 Two-player interactive mode
- 🧠 Full win-condition logic (horizontal, vertical, diagonal)
- ♻️ Game reset functionality
- 🚫 Button lock after move to prevent cheating
- 💡 Visual cues for winning tiles (turns green)
- 🔄 PyQt5 `.ui` file-based interface using `uic.loadUi()`

---

## 📷 Screenshots

*(Add your screenshots here after UI build)*

---

## 🗂 Project Structure

```

tictactoe/
├── main.py           # Main game logic using PyQt5
├── tictactoe.ui      # UI layout created via Qt Designer
└── README.md         # This README file

````

---

## ⚙️ Installation

### 🐍 Prerequisites

- Python 3.x
- `PyQt5` library

### 📦 Install Dependencies

```bash
pip install PyQt5
````

> 💡 Tip: Use a virtual environment for cleaner dependency management.

---

## ▶️ Usage

1. Clone or download the repository.
2. Ensure `tictactoe.ui` is in the same folder as `main.py`.
3. Run the game using:

```bash
python main.py
```

---

## 🖌 UI Details

The `.ui` file (`tictactoe.ui`) contains:

* `QPushButton`s named by position (`zero0`, `zero1`, ..., `two2`) representing the 9 cells.
* A `QLabel` named `label0` to display game status (e.g., "X's Turn", "O Wins!").
* A `QPushButton` named `resetButton` to restart the game.

UI is loaded at runtime using:

```python
uic.loadUi("tictactoe.ui", self)
```

---

## 🧩 Game Logic

1. **Turn Tracking:**

   * Alternates between X and O using a simple `turn` counter (`self.turn % 2`).

2. **Button Click Handling:**

   * Disables the clicked button.
   * Sets the mark (`X` or `O`).
   * Updates status label.

3. **Win Detection:**

   * Checks 8 possible winning combinations after each move.
   * Highlights winning buttons in green.
   * Freezes further input on game end.

4. **Draw Detection:**

   * Checks if all 9 tiles are filled without a win.
   * Declares a draw and disables all buttons.

5. **Reset Functionality:**

   * Clears text, restores button state, resets color and turn.

---

## 🔍 Code Overview (main.py)

* `MainWindow`: Inherits from `QMainWindow`, houses UI logic.
* `gridFill()`: Handles cell marking and triggers win/draw check.
* `checkWin()`: Evaluates all winning conditions.
* `win()`: Displays winner and highlights tiles.
* `khichdi()`: Declares a draw if the board is full with no winner.
* `freeze()`: Disables all board buttons.
* `startOver()`: Resets the board and game state.

---

## 🚀 Future Improvements

* 🎨 Enhanced UI/UX (add animations or hover effects)
* 🔊 Sound effects for moves and wins
* 🤖 AI opponent using minimax for single-player mode
* 📱 PyQt6 or mobile-optimized layout
* 🌐 Web version using Flask + PyScript

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute with credit.

---
