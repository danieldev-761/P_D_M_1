# Function to validate user input
def validate_input(prompt, type_func, condition=None, error_msg="Invalid Input.", allow_empty= False):
    """
    Validates user input.

    Parameters:
    prompt (str): The prompt message to display.
    type_func (function): The function to convert the input (e.g., int, float, bool).
    condition (function, optional): A condition function to check validity.
    error_msg (str): The error message to display on invalid input.
    allow_empty (optional): It is used in case you want to skip an update or modification of a variable

    Returns:
    The converted and validated value.
    """

    
    valid = False
    while not valid:
                
        user_input = input(prompt)
        try:
            if allow_empty and user_input == "":
                return None
            else: 
                value = type_func(user_input)
                if condition and not condition(value):
                    print(error_msg)
                    continue
                valid = True
                return value
        except ValueError:
            print(error_msg)




def add_students(students, ID, name, age, course, status):

    """
    Adds a new student to the students list.

    Parameters:
    students (list): The list of students in the list.
    ID (int): Identification number of the student
    name (str): The name of the student.
    age (int): The age of the student.
    course (str): The name of the program/course the student is taking.
    status (bool): Student's inactive or active status

    Returns:
    list: The updated student list with the new student added.
    """
    # Create student dictionary
    student = {
        "ID": ID,
        "name": name,
        "age": age,
        "course": course,
        "status": status
    }

    # Append to students list
    students.append(student)
    return students


def show_students(students):
    """
    Displays the students.

    Parameters:
    students (list): The list of students.

    Returns:
    str: A string representation of the students list.
    """
    if not students:
        return "The student list is currently empty. No students to show.\n"
    result = ""
    for student in students:
        result += f"ID: {student['ID']} | Name: {student['name']} | Age: {student['age']} | Course/Program: {student['course']} | Status: {student['status']}\n"
    return result

def search_students(students):
    """
    If students list is not None: Searches for a student by name or ID in the list.

    Parameters:
    students (list): The list of students.

    Returns:
    dict or None: The student dictionary if found, None otherwise.
    """
    
    if not students:
        print("The students list is currently empty. No students to search.\n")
        return None
    
    #input (str): The name or ID of the student to search for.
    #validate the input for student name or ID, if the input is invalid, show an error message and ask for input again

    found= False
    search_input = validate_input("Enter the student name or ID to search: ", 
                            str, 
                            lambda x: x.strip() != "", 
                            "Error: Search input cannot be empty. Please enter a valid input (ID or name).").capitalize()
    
    
    for student in students:
        if student['name'] == search_input or str(student['ID']) == search_input:
            found= True
            return student
        
        
    if not found:
        print(f"Student '{search_input}' not found in the inventory.\n")
            

    return False

# Function to update a student's information
def update_students(students, new_name= None, new_age=None, new_course=None, new_status= None):
    """
    If Students list is not None: Updates the info of a student in the inventory, optional items.

    Parameters:
    inventory (list): The list of students in the inventory.
    new_name (str, optional): The new name of the student to update.
    new_age(int, optional): The new age for the student.
    new_course (str, optional): The new course/program for the student.
    new_ status (bool, optional): The new status (inactive: 0, active: 1) for the student

    Returns:
    bool: True if the student was updated, False if not found.
    """

    #validate the input for student name, if the input is invalid, show an error message and ask for input again
    search_input = validate_input("Enter the student name or ID to update: ", str, lambda x: x.strip() != "", "Error: student name or ID cannot be empty. Please enter a valid input.").capitalize()
            
    for student in students:
        if student['name'] == search_input or student['ID'] == search_input:
            if new_name is not None:
                student['name'] = new_name
            if new_age is not None:
                student['age'] = new_age
            if new_course is not None:
                student['course'] = new_course
            if new_status is not None:
                student['status'] = new_status
            return True
        
        else:
            print(f"Failed to update student '{search_input}'.\n")
    return False

# Function to delete a student by name
def delete_students(students):


    """
    If Inventory is not None: Removes a student from the inventory by name.

    Parameters:
    inventory (list): The list of students in the inventory.
    input (str): The name or ID of the student to remove.

    Returns:
    bool: True if the student was removed, False if not found.
    """
    #validate the input for student name, if the input is invalid, show an error message and ask for input again
    search_input = validate_input("Enter the student name or ID to delete: ", str, lambda x: x.strip() != "", "Error: student name or ID cannot be empty. Please enter a valid input.").capitalize()

    
    for i, student in enumerate(students):
        if student['name'] == search_input or student['ID'] == search_input:

            confirm= input("Are you completely sure about? Once you delete a student, all their information will be lost: (Y/N)").strip().upper()

            if confirm == "Y":

                del students[i]
                return True
            
            return False
    return False


