# Hangman Game 🎮

A simple terminal-based Hangman game built with **Python**. The player tries to guess a randomly selected English word, one letter at a time, before running out of attempts.

## Features

- Random word selection from an external text file.
- Six incorrect attempts allowed.
- ASCII Hangman graphics that update after incorrect guesses.
- Tracks correctly and incorrectly guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Validates user input.
- Displays the remaining attempts and hidden word.
- Shows win or game-over messages.

## Technologies Used

- **Language:** Python 3
- **Module:** `random`
- **Concepts:** Variables, strings, lists, sets, loops, conditional statements, file handling, and built-in functions.

## Project Structure

```text
Hangman-Game/
│
├── hangman.py
├── englishwordlist.txt
└── README.md
```

| File | Description |
|---|---|
| `hangman.py` | Main Python game program |
| `englishwordlist.txt` | External list of English words |
| `README.md` | Project documentation |

## Requirements

- Python 3.x
- An English word list saved as `englishwordlist.txt`

No external Python packages are required.

## How to Run

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Hangman-Game
```

**3. Run the Python program**

```bash
python hangman.py
```

Make sure `englishwordlist.txt` is in the same directory as `hangman.py`.

## How to Play

1. Run the program.
2. A random English word is selected.
3. The hidden word appears as underscores.
4. Enter one alphabetic letter at a time.
5. Correct guesses reveal the matching letters.
6. Incorrect guesses reduce your remaining attempts.
7. Guess the complete word before six incorrect attempts to win.

## Example Gameplay

```text
      +---+
      |   |
      O   |
          |
          |
    =========

Word: _ P _ T H _ N

Remaining attempts: 5

Correct guesses: ['H', 'P']
Wrong guesses: ['A']

Enter guess letter:
```

## Learning Objectives

This project helped me practice:

- Working with Python lists and sets.
- Reading external text files.
- Using loops and conditional statements.
- Handling user input and validating data.
- Using functions from Python's built-in modules.
- Managing game states and tracking attempts.
- Building a command-line application.

## Future Improvements

- Add difficulty levels (Easy, Medium, Hard).
- Add hints for difficult words.
- Display a score system.
- Organize the program using Python functions.
- Add a graphical user interface (GUI).

## Author

Naima Sultana

Software Engineering Student


---

*Built as a beginner Python programming project to practice fundamental programming concepts.*
