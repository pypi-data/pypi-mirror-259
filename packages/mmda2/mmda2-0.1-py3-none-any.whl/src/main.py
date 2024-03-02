from os import system
from time import sleep

student_list = []

def clear_screen():
    system("cls")

def add_student():
    clear_screen()
    updated_student = {}

    while True:
        name = input("Name: ")
        if name.isalpha():
            updated_student["name"] = name
            break
        print("Error! Please enter a valid name.")
        sleep(1)
        clear_screen()

    while True:
        last_name = input("Last Name: ")
        if last_name.isalpha():
            updated_student["last name"] = last_name
            break
        print("Error! Please enter a valid last name.")
        sleep(1)
        clear_screen()

    while True:
        age = input("Age: ")
        if age.isdigit() and 0 < int(age) <= 120:
            updated_student["age"] = int(age)
            break
        print("Error! Please enter a valid age (1-120).")
        sleep(1)
        clear_screen()

    while True:
        gender = input("Gender (1: Male, 2: Female, 3: Other) : ")
        if gender in ["1", "2", "3"]:
            genders = ["Male", "Female", "Other"]
            updated_student["gender"] = genders[int(gender) -1]
            break
        print("Error! Please enter a valid gender option /: ")
        sleep(1)
        clear_screen()

    while True:
        student_code = input("Student Code: ")
        if student_code.isdigit() and int(student_code) not in [student["student code"] for student in student_list]:
            updated_student["student code"] = int(student_code)
            break
        print("Error! Please enter a valid and unique student code.")
        sleep(1)
        clear_screen()

    while True:
        national_code = input("National Code: ")
        if national_code.isdigit() and int(national_code) not in [student["national code"] for student in student_list]:
            updated_student["national code"] = int(national_code)
            break
        print("Error! Please enter a valid and unique national code.")
        sleep(1)
        clear_screen()

    while True:
        javascore = input("Java Score: ")
        if 0 <= float(javascore) <= 100:
            updated_student["java score"] = float(javascore)
            break
        print("Error! Please enter a valid Java score (0-100).")
        sleep(1)
        clear_screen()

    while True:
        pythonscore = float(input("Python Score: "))
        if 0 <= pythonscore <= 100:
            updated_student["python score"] = float(pythonscore)
            break
        print("Error! Please enter a valid Python score (0-100).")
        sleep(1)
        clear_screen()

    while True:
        phpscore = input("Php Score: ")
        if 0 <= float(phpscore) <= 100:
            updated_student["php score"] = float(phpscore)
            break
        print("Error! Please enter a valid PHP score (0-100).")
        sleep(1)
        clear_screen()

    student_list.append(updated_student)
    print("successfully!")
    sleep(1)
    clear_screen()

def show_students():
    clear_screen()
    if not student_list:
        
        print("No student exist !\n")
        input("Press Enter to continue")
        return

    while True:
        system("cls")
        if input("Do you want to display all columns? (yes/etc): ") == "yes":
            system("cls")
            print("ID\tName\tLname\tAge\tGender \tSTcode \tNTcode\tjaScore\tpyScore\tphpScore")
            print("_" * 80)
    
            for id_, student_ in enumerate(student_list, 1):
                print(id_, end="\t")
                print(student_["name"], end="\t")
                print(student_["last name"], end="\t")
                print(student_["age"], end="\t")
                print(student_["gender"], end="\t")
                print(student_["student code"], end="\t")
                print(student_["national code"], end="\t")
                print(student_["java score"], end="\t")
                print(student_["python score"], end="\t")
                print(student_["php score"])
            input("\n\nPress Enter to continue.")
            break
        else:
            display_columns = ["Name", "last name", "age", "gender", "student code", "national code" , "java score" , "python score" , "php score"]
            display_indices = []
            for column in display_columns:
                if input("Do you want to display " + column + "? (yes/etc):") == "yes":
                    display_indices.append(display_columns.index(column))

            if not display_indices:
                print("No columns selected.")
                break

            print("ID\t", end="")
            for index in display_indices:
                print(display_columns[index], end="\t")
            print("\n" + "_" * 80)

            for id_, student_ in enumerate(student_list, 1):
                print(id_, end="\t")
                for index in display_indices:
                    column_name = display_columns[index]
                    print(student_.get(column_name, ""), end="\t")
                print()
            input("Press Enter to continue.")
            break
    clear_screen()

def remove_student():
    clear_screen()
    if not student_list:
        print("No students exist!")
        input("Press Enter to continue.")
        clear_screen()
        return

    while True:
        removal_option = input("1. Remove by student code\n2. Remove by national code\n3. Cancel\n\nEnter option: ")
        if removal_option == "1":
            student_code = input("Enter student code to remove: ")

            if student_code.isdigit():
                student_code = int(student_code)
                
                if any(student["student code"] == student_code for student in student_list):
                    student_list[:] = [student for student in student_list if not student["student code"] == student_code]
                    print("Removing...")
                    sleep(1)
                    clear_screen()
                    return
                else:
                    print("Error: Student code not found.")
                    sleep(1)
                    clear_screen()
            else:
                print("Error: Invalid student code.")
                sleep(1)
                clear_screen()
        elif removal_option == "2":
            national_code = input("Enter national code to remove: ")
            if national_code.isdigit():
                national_code = int(national_code)
                if any(student["national code"] == national_code for student in student_list):
                    student_list[:] = [student for student in student_list if not student["national code"] == national_code]
                    print("Removing...")
                    sleep(1)
                    clear_screen()
                    return
                else:
                    print("Error: National code not found.")
                    sleep(1)
                    clear_screen()
            else:
                print("Error: Invalid national code.")
                sleep(1)
                clear_screen()
        elif removal_option == "3":
            return
        else:
            print("Invalid option! Please select again.")
            sleep(1)
            clear_screen()

def edit_student():
    clear_screen()
    if not student_list:
        print("No students exist!")
        input("Press Enter to continue.")
        clear_screen()
        return

    while True:
        edit_option = input("1. Edit by student code\n2. Edit by national code\n3. Cancel\n\nEnter option: ")
        if edit_option == "1":
            student_code = input("Enter student code to edit: ")
            if not student_code.isdigit():
                print("Error: Invalid student code.")
                sleep(1)
                clear_screen()
                continue
                
            student_code = int(student_code)
            for student in student_list:
                if student["student code"] == student_code:
                    updated_student = updated_students_data(student)
                    student_list[student_list.index(student)] = updated_student
                    print("updated successfully!")
                    sleep(1)
                    clear_screen()
                    return
            print("Error: Student code not found.")
            sleep(1)
            clear_screen()
                
        elif edit_option == "2":
            national_code = input("Enter national code to edit: ")
            if not national_code.isdigit():
                print("Error: Invalid national code.")
                sleep(1)
                clear_screen()
                continue
                
            national_code = int(national_code)
            for student in student_list:
                if student["national code"] == national_code:
                    updated_student = updated_students_data(student)
                    student_list[student_list.index(student)] = updated_student
                    print("updated successfully!")
                    sleep(1)
                    clear_screen()
                    return
            print("Error: National code not found.")
            sleep(1)
            clear_screen()
                
        elif edit_option == "3":
            return
        else:
            print("Invalid option! select again.")
            sleep(1)
            clear_screen()

def updated_students_data(student):
    updated_student = student.copy()
    system("cls")
    print("\t\tEnter new info (leave it empty to keep current) :\n")
    updated_student["name"] = input(f"Name [{student['name']}]: ") or student["name"]
    updated_student["last name"] = input(f"Last Name [{student['last name']}]: ") or student["last name"]
    updated_student["age"] = input(f"Age [{student['age']}]: ") or student["age"]
    updated_student["gender"] = input(f"Gender [{student['gender']}]: ") or student["gender"]
    updated_student["student code"] = input(f"Student Code [{student['student code']}]: ") or student["student code"]
    updated_student["national code"] = input(f"National Code [{student['national code']}]: ") or student["national code"]
    updated_student["java score"] = input(f"Java Score [{student['java score']}]: ") or student["java score"]
    updated_student["python score"] = input(f"Python Score [{student['python score']}]: ") or student["python score"]
    updated_student["php score"] = input(f"PHP Score [{student['php score']}]: ") or student["php score"]
    return updated_student

def best_student():
    clear_screen()
    if not student_list:
        print("No students exist!")
        input("Press Enter to continue.")
        return

    best_student = max(student_list , key=lambda student : (student["java score"] + student["python score"] + student["php score"]) / 3)
    avg_score = round((best_student["java score"] + best_student["python score"] + best_student["php score"]) / 3, 2)
    
    print("Best Student by Top Scores:\n")
    print("Name\tLname\tAge\tGender\tSTcode\tNTcode\tjsScore\tpyScore\tphpScore  AVG")
    print("_" * 100)

    for key , value in best_student.items():
        print(value, end="\t")
    print(avg_score)
    input("\nPress Enter to continue.")

def search_student():
    clear_screen()
    if not student_list:
        print("No students exist!")
        input("Press Enter to continue.")
        return

    while True:
        print("Search by:\n")
        print("1. Name")
        print("2. Last Name")
        print("3. Student Code")
        print("4. National Code")
        print("5. Gender")
        print("6. Back")
        search_option = input("Enter option: ")

        if search_option == "6":
            clear_screen()
            break

        elif search_option in ["1", "2", "3", "4", "5"]:
            search_term = input("Enter search term: ")

            if search_option == "1":
                key = "name"

            elif search_option == "2":
                key = "last name"

            elif search_option == "3":
                key = "student code"

            elif search_option == "4":
                key = "national code"
                
            elif search_option == "5":
                key = "gender"

            search_results = [student for student in student_list if search_term.lower() == student[key].lower()]

            if search_results:
                print("Search Results:\n")
                print("ID\tName\tLname\tAge\tGender\tSTcode\tNTcode\tJsScore\tPyScore\tphpScore")
                print("_" * 100)

                for id_, student_ in enumerate(search_results, 1):
                    print(f"{id_}\t{student_['name']}\t{student_['last name']}\t{student_['age']}\t{student_['gender']}\t"
                          f"{student_['student code']}\t{student_['national code']}\t{student_['java score']}\t"
                          f"{student_['python score']}\t{student_['php score']}")
            else:
                print("\nNo results found.")

            input("\nPress Enter to continue.")
            clear_screen()

        else:
            print("Invalid option. Enter a valid option.")
            sleep(1)
            clear_screen()

def main():
    while True:
        clear_screen()
        print("\n_________ Menu _________")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Remove Student")
        print("4. Edit Student")
        print("5. Best Student")
        print("6. Search Student")
        print("7. Exit")
        print("________________________")

        menu = input("Menu: ")

        if menu == "7":
            clear_screen()
            print("S33 u")
            break

        elif menu == "1":
            add_student()

        elif menu == "2":
            show_students()

        elif menu == "3":
            remove_student()

        elif menu == "4":
            edit_student()

        elif menu == "5":
            best_student()

        elif menu == "6":
            search_student()

        else:
            print("Invalid option! try again.")
            sleep(1)
            clear_screen()

if __name__ == "__main__":
    main()
