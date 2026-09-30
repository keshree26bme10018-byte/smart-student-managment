# Smart Student Management System

A beginner-friendly, menu-driven student record management application
built with **Python**. The project lets users add student details,
validates input, prevents duplicate roll numbers, and stores records in
a CSV file.

## Features

-   Add a student's roll number, name, branch, and marks
-   Validate that required fields are not empty
-   Check that marks are numeric and between 0 and 100
-   Prevent duplicate roll numbers
-   Save student records in `students.csv`
-   Keep the menu running until the user chooses to exit

## Technologies Used

-   **Python 3**
-   **Visual Studio Code**
-   Python's built-in `csv` module
-   Python's built-in `os` module

No third-party Python packages are required.

## Project Structure

``` text
Smart-Student-Management/
├── app.py                         # Original starter file (if retained)
├── smart student managment.py     # Main program (current filename)
└── students.csv                   # Created automatically after adding a student
```

> **Tip:** For a simpler command, rename `smart student managment.py` to
> `main.py`. If you do, use `python main.py` in the instructions below.

## How to Run

1.  Install Python 3 if it is not already installed.

2.  Open this project folder in Visual Studio Code.

3.  Open the terminal in VS Code (**Terminal → New Terminal**).

4.  Run the program. If you kept the current filename, use:

    ``` bash
    python "smart student managment.py"
    ```

    If you renamed the file to `main.py`, use:

    ``` bash
    python main.py
    ```

5.  When the menu appears:

    -   Enter `1` to add a student.
    -   Enter the requested student details.
    -   Enter `2` to exit.

## Example

``` text
Welcome to Smart Student Management System!

1. Add Student
2. Exit
Enter your choice: 1
Enter Roll Number: 101
Enter Student Name: Priya Sharma
Enter Branch: Mechanical
Enter Marks (out of 100): 85

Student added successfully!
```

## Data Storage

Student records are saved in `students.csv` in the working directory.
The file is created automatically when the first student is added. It
contains these columns:

  Roll Number   Name           Branch       Marks
  ------------- -------------- ------------ -------
  101           Priya Sharma   Mechanical   85.0

You can open the CSV file in a text editor or spreadsheet application.

## Concepts Practised

-   Functions
-   User input and output
-   Conditional statements
-   `while` loops
-   `try-except` exception handling
-   File handling
-   CSV reading and writing

## Current Limitations

This version supports adding student records and exiting the
application. It does not yet include options to view, search, update, or
delete existing records, and it does not use a database or login system.

## Future Improvements

-   Display all student records
-   Search for a student by roll number
-   Update and delete records
-   Use SQLite for data storage
-   Add a graphical user interface
-   Add subject-wise marks and grade calculation

## Author

**Keshree Galphat**\
B.Tech Mechanical Engineering\
VIT Bhopal University

------------------------------------------------------------------------

This project was created as a learning project to practise Python
programming and basic file handling.
