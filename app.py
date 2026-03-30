from services import *


#initialize students list 
students= []

print("Hi. Welcome to our Student Management System! \n")

active= 1

#main menu loop: while active is 1, the menu will keep showing, if the user chooses to exit, it will change to 0 and the loop will end    
while active == 1:



    print(f""" {'-'*30}OPTIONS MENU{'-'*30}

    1. Add new students.
    2. Show all students.
    3. Search only one student by criteria (e.g., ID or name).
    4. Update the information about a student.
    5. Delete students 
    6. Exit      \n""")



    option= input("Enter the number of the option to select: ")

    match option:

        case "1":

            keep_adding= 1

            while keep_adding == 1:

                print(f"{'-'*20} STUDENT ADDITION MODULE {'-'*20}")

                
                ID= validate_input("Enter a valid student ID: ", 
                                    int,  
                                    lambda x: x >= 0 and x not in [student['ID'] for student in students], 
                                    "Error:  Student ID cannot be negative, empty or already existing. Please enter a valid ID.")

                name= validate_input("Enter the student name: ", 
                                    str, 
                                    lambda x: x.strip() != "" and not x.isdigit(), 
                                    "Error: Student name cannot be empty or only digit. Please enter a valid name.").capitalize()
                
                age= validate_input("Enter a valid student age: ", 
                                    int,  
                                    lambda x: x >= 5, 
                                    "Error:  Age cannot be negative or empty. Please enter a valid ID.")
                
                course= validate_input("Enter the student course/program: ", 
                                    str, 
                                    lambda x: x.strip() != "" and not x.isdigit(), 
                                    "Error: Student course cannot be empty or only digit. Please enter a valid course.").capitalize()
                
                status= validate_input("Enter the student status (active= 1 /inactive = 0): ", 
                                    int, 
                                    lambda x: x == 0 or x==1,
                                    "Error: Student status cannot be empty or out of range (only 0-1). Please enter a valid status.")
                
                status= "active" if status== 1 else "inactive"
                add_students(students, ID, name, age, course, status)

                print(f"Student with ID: '{ID}' | Name: '{name}' added successfully. \n") 
                
                
                
                # ask the user if they want to keep adding students, if they choose to continue
                keep_adding= (input("Do you want to continue adding students? (1 for Yes, another number or char for No): "))
                keep_adding= int(keep_adding) if keep_adding.isdigit() else 0
                
                print("You chose continue adding another student \n") if keep_adding==1 else print("Returning to the main menu... \n")



        case "2":
            print(f"{'-'*20} STUDENT DISPLAY MODULE {'-'*20}")

            result= show_students(students)

            print(result)

        case "3":
            print(f"{'-'*20} STUDENT SEARCH MODULE {'-'*20}")

            #call the function to search the student and store the result in a variable
            found_student = search_students(students)
            
            #show a message personlized depending on the result of the search
            if found_student:
                print(f"Student found: ID: {found_student['ID']} | Name: {found_student['name']} | Age: {found_student['age']} | Course/Program: {found_student['course']} | Status: {found_student['status']}\n")      
                
        case "4":
            print(f"{'-'*20} STUDENT UPDATE MODULE {'-'*20}")

            if not students:
                print("The students list is currently empty. No students to update.\n")
    
            else: 

                #call the function to search the student and store the result in a variable
                found_student = search_students(students)
                
                #show a message personalized depending on the result of the search
                if found_student:
                    print(f"Student found: ID: {found_student['ID']} | Name: {found_student['name']} | Age: {found_student['age']} | Course/Program: {found_student['course']} | Status {found_student['status']}\n")
                    
                    #ask for new optional items to update
                    new_name= validate_input("Enter the student name: ", 
                                        str, 
                                        lambda x: x.strip() != "" and not x.isdigit(), 
                                        "Error: Student name cannot be empty or only digit. Please enter a valid name.",
                                        allow_empty=True)
                    
                    new_name= new_name.capitalize() if new_name != None else None
                    
                    new_age= validate_input("Enter a valid student age: ", 
                                        int,  
                                        lambda x: x >= 5, 
                                        "Error:  Age cannot be negative or empty. Please enter a valid ID.",
                                        allow_empty=True)
                    
                    
                    
                    new_course= validate_input("Enter the student course/program: ", 
                                        str, 
                                        lambda x: x.strip() != "" and not x.isdigit(), 
                                        "Error: Student course cannot be empty or only digit. Please enter a valid course.",
                                        allow_empty=True)
                    
                    new_course= new_course.capitalize() if new_course != None else None
                    
                    
                    new_status= validate_input("Enter the student status (active= 1 /inactive = 0): ", 
                                    int, 
                                    lambda x: x == 0 or x==1,
                                    "Error: Student status cannot be empty or out of range (only 0-1). Please enter a valid status.",
                                    allow_empty= True)
                
                    new_status= "active" if status== 1 else "inactive"
                    
                    if new_name is None:
                        new_name = found_student["name"]

                    if new_age is None:
                        new_age = found_student["age"]

                    if new_course is None:
                        new_course = found_student["course"]

                    if new_status is None:
                        new_status = found_student["status"]

                    

                    
                    #call the function to update the student and show a success message
                    if update_students(students, new_name, new_age, new_course, new_status):
                        print(f"student updated successfully.\n")
                
                else:
                    print(f"student not found in the students list\n")

        case "5":
            print(f"{'-'*20} STUDENT DROP MODULE {'-'*20}")

            if not students:
                print("The students list is currently empty. No students to delete.\n")

            else:

                #validate the input for student name, if the input is invalid, show an error message and ask for input again
                search_input = validate_input("Enter the student name or ID to delete: ", str, lambda x: x.strip() != "", "Error: student name or ID cannot be empty. Please enter a valid input.").capitalize()

                #call the function to delete the student and show a message personalized depending on the result
                if delete_students(students, search_input):
                    print(f"student {search_input} deleted successfully from the students list.\n")
                else:
                    print(f"student {search_input} not found in the the students list. No deletion performed.\n")
        

        case "6":
            print("Thank you for using the program. Exiting...")
            active= 0

        case _:
            print("Invalid option. Please input a valid one (1-6). \n")



        





