# Students Management System with collections 

This repository contains a Python program that allows users to manage a students list through a console-based menu system.

The system includes:

* Add, show, search, update, and delete students
* Input validation and error handling
* Menu-based interaction with continuous execution

The project is designed as a programming fundamentals exercise, covering:

* Console input/output handling
* Data structures (lists and dictionaries)
* Control flow (loops and conditionals)
* Basic validation and error handling


## Features

- CRUD operations (Add, Search, Update, Delete)
- Input validation with error handling



## Usage

To run the program:

1. Open a terminal and navigate to the project directory
2. Ensure Python 3 is installed (`python3 --version`)
3. Run the script: `python3 app.py`
4. Use the menu to interact with the system:

   * Add students
   * Show Students
   * Search, update, or delete students
   * Exit the program

Follow the on-screen instructions for each option.

## Example Execution

```
--------------------INVENTORY MENU--------------------
    1. Add new students.
    2. Show all students.
    3. Search only one student by criteria (e.g., ID or name).
    4. Update the information about a student.
    5. Delete students 
    6. Exit   


Enter the number of the option to select: 1
-------------------- STUDENT ADDITION MODULE --------------------
Enter a valid student ID: 1
Enter the student name: Andres
Enter a valid student age: 15
Enter the student course/program: 10c
Enter the student status (active= 1 /inactive = 0): 1
Student with ID: '1' | Name: 'Andres' added successfully. 

Do you want to continue adding students? (1 for Yes, another number or char for No): no
Returning to the main menu... 
```

## Project Structure

Core files:

- app.py           - Main program
- services.py     - Business logic

Other:

- README.md
- LICENSE
- .gitignore

## GitHub: https://github.com/danieldev-761/P_D_M_1/t

## Author

* Daniel Echeverría, Coder Riwi

## License

This project is distributed under the GNU General Public License (GPL). See the LICENSE file for more details.