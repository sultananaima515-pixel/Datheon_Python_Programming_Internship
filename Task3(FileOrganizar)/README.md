# Task 3: File Organizer

## Overview
The File Organizer is a Python-based project that automatically organizes files into separate folders according to their file extensions.

Instead of manually sorting files, the program scans a selected directory, identifies file types, creates category folders when needed, and moves files into their corresponding folders.

## Features
- Scans files in a specified directory.
- Identifies file types using file extensions.
- Organizes files into category-based folders.
- Creates destination folders automatically.
- Moves files using Python file-handling operations.
- Handles duplicate filenames to avoid overwriting existing files.
- Includes exception handling for file operations.

## Technologies Used
- Python 3
- `os` module
- `pathlib` module
- `shutil` module

## Project Structure

```text
Task3(FileOrganizar)/
│
├── main.py
├── README.md
│
└── testdownloads/
    ├── Images/
    ├── Documents/
    ├── Videos/
    └── Others/
```

*Note: The folders inside `testdownloads` are example categories. Your actual folder names depend on the extension categories defined in your program.*

## How It Works

1. The program accesses the source directory.
2. It scans the files inside the directory.
3. It extracts each file's extension.
4. It identifies the appropriate category using an extension mapping.
5. It creates the destination folder if it does not already exist.
6. It moves the file into the corresponding folder.
7. It handles duplicate filenames and file-operation errors.

## Python Concepts Used
- Variables and dictionaries
- Conditional statements
- Loops
- Functions
- File handling
- File extensions
- Directory management
- Exception handling
- Modules and libraries

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Make sure the source directory exists.
4. Open the terminal.
5. Run:

```bash
python main.py
```

6. Check the output directory to see the organized files.

## Learning Outcomes
- Learned how to work with files and directories in Python.
- Practiced using `os`, `pathlib`, and `shutil`.
- Understood file extensions and directory structures.
- Implemented automatic file organization.
- Practiced handling duplicate filenames and file-operation errors.

## Project Type
Python Programming Internship — Task 3
