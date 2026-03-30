from services import *



students= []

print("Hi. Welcome to our Student Management System! \n")

active= 1


while active == 1:



    print(f""" {'-'*30}OPTIONS MENU{'-'*30}

    1. Add new students.
    2. Show all students.
    3. Search only one student by criteria (e.g. ID or name).
    4. Update the information about a student.
    5. Delete students 
    6. Exit      \n""")



    option= input("Enter the number of the option to select: ")

    match option:

        case "1":
            print(f"{'-'*20} STUDENT ADDITION MODULE {'-'*20}")


        case "2":
            print(f"{'-'*20} STUDENT DISPLAY MODULE {'-'*20}")

        case "3":
            print(f"{'-'*20} STUDENT SEARCH MODULE {'-'*20}")

        case "4":
            print(f"{'-'*20} STUDENT UPDATE MODULE {'-'*20}")

        case "5":
            print(f"{'-'*20} STUDENT DROP MODULE {'-'*20}")

        case "6":
            print("Thank you for using the program. Exiting...")
            active= 0

        case _:
            print("Invalid option. Please input a valid one (1-6). \n")



    





