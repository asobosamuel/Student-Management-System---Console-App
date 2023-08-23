import json
from csv import DictWriter


students = []
list_of_subjects = ['Biology', 'Chemistry', 'Physics', 'Mathematics', 'Further Maths', 'Comp. Sc']


def calculate_grade(student_id):
    total_score = 0
    for subject in students[student_id]['subjects']:
        total_score += subject['subject_score']
    average = round(total_score / len(students[student_id]["subjects"]), 2)
    if 80 <= average <= 100:
        grade = "A"
    elif 70 <= average <= 79:
        grade = "B+"
    elif 60 <= average <= 69:
        grade = "B"
    elif 55 <= average <= 59:
        grade = "C+"
    elif 50 <= average <= 54:
        grade = "C"
    elif 45 <= average <= 49:
        grade = "D+"
    elif 40 <= average <= 44:
        grade = "D"
    else:
        grade = "F"
    students[student_id]["grade"] = grade
    students[student_id]["average"] = average


def display_subjects():
    for i in range(len(list_of_subjects)):
        if i % 4 == 0:
            print(f"\n{i}. {list_of_subjects[i]}\t|\t", end="")
        else:
            print(f"{i}. {list_of_subjects[i]}\t|\t", end="")
    print()


def add_student():
    name = input("Enter name of Student: ")
    while True:
        try:
            age = int(input("Enter the age of student: "))
        except ValueError:
            print('Enter a number!!!')
        else:
            break
    display_subjects()
    subjects = []
    for subject in list_of_subjects:
        while True:
            try:
                subject_score = int(input(f"Enter {name}'s score for {subject} /100: "))
            except ValueError:
                print('Enter a number!!!')
            else:
                break

        subjects.append({"subject_title": subject, "subject_score": subject_score})
        print("------------------------------------------------------------------------")
    student_info = {"name": name,
                    "age": age,
                    "subjects": subjects}
    students.append(student_info)
    calculate_grade(len(students) - 1)
    save_students_to_file()


def update_student():
    print("\tStudent ID\t|\tName")
    for student_id, student in enumerate(students):
        print(f"\t{student_id}\t\t|\t{student['name']}")
    while True:
        try:
            selected_student = int(input("Enter the student ID: "))
        except ValueError:
            print('Enter a number!!!')
        else:
            break

    print("What info do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Name & Age")
    while True:
        while True:
            try:
                option = int(input("Enter your choice: "))
            except ValueError:
                print('Enter a number!!!')
            else:
                break

        if option == 1:
            name = input("Enter new name: ")
            students[selected_student]["name"] = name
            print("...Name updated successfully...")
            break
        elif option == 2:
            age = input("Enter new age: ")
            students[selected_student]["age"] = age
            print("...Age updated successfully...")
            break
        elif option == 3:
            name = input("Enter new name: ")
            students[selected_student]["name"] = name
            age = input("Enter new age: ")
            students[selected_student]["age"] = age
            print("...Name & Age updated successfully...")
            break
        else:
            print("Enter either 1 or 2!!!")
    print("Updated Info:")
    print(
        f"\tstudent ID: {selected_student}\n\tName: {students[selected_student]['name']}\n\tAge: {students[selected_student]['age']}")
    save_students_to_file()


def delete_student():
    print("\tStudent ID\t|\tName")
    for student_id, student in enumerate(students):
        print(f"\t{student_id}\t\t|\t{student['name']}")
    while True:
        try:
            selected_student = int(input("Enter the ID of the student you want to delete: "))
        except ValueError:
            print('Enter a number!!!')
        else:
            break

    del students[selected_student]
    print("...Student deleted successfully...")
    save_students_to_file()


def display_grades():
    print("\tStudent ID\t|\tName\t|\tGrade\t|\tAverage")
    for student_id, student in enumerate(students):
        print(f"\t{student_id}\t\t|\t{student['name']}\t\t|\t{student['grade']}\t\t|\t{student['average']}")


def display_students():
    for student_id, student in enumerate(students):
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Average: {student['average']}")
        print(f"Grade: {student['grade']}")
        print("Subjects:")
        for subject in student["subjects"]:
            print(f"\t{subject['subject_title']}\tScore: {subject['subject_score']} |", end="")
        print("\n----------------------------------------------------------------------------------------------------------------------------------------------------")


def calculate_average_grade():
    total = 0
    for student in students:
        total += student['average']
    average_grade = round(total / len(students), 2)
    print("Average Grade: " + str(average_grade))
    return average_grade


def get_highest_grade():
    max_index = 0
    for i in range(1, len(students)):
        if students[i]['average'] > students[max_index]['average']:
            max_index = i
    highest_grade = students[max_index]['grade']
    print(f"Highest Grade: {highest_grade} By {students[max_index]['name']}")
    return highest_grade


def get_lowest_grade():
    min_index = 0
    for i in range(1, len(students)):
        if students[i]['average'] < students[min_index]['average']:
            min_index = i
    lowest_grade = students[min_index]['grade']
    print(f"Lowest Grade: {lowest_grade} By {students[min_index]['name']}")
    return lowest_grade


def get_user_choice():
    while True:
        while True:
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print('Enter a number!!!')
            else:
                break

        print("\n")
        if choice in range(1, 12):
            return choice
        print("choice out of range ( 1 - 11 )!!!!!")


def execute_user_choice(choice_id):
    if choice_id == 1:
        display_students()
    elif choice_id == 2:
        display_grades()
    elif choice_id == 3:
        add_student()
    elif choice_id == 4:
        update_student()
    elif choice_id == 5:
        delete_student()
    elif choice_id == 6:
        calculate_average_grade()
    elif choice_id == 7:
        get_highest_grade()
    elif choice_id == 8:
        get_lowest_grade()
    elif choice_id == 9:
        generate_report()
    elif choice_id == 10:
        save_students_to_file()
    else:
        save_students_to_file()
        print("Exiting....")
        exit()


def display_menu():
    print("\nWelcome to the student management system...")
    while True:
        print("What do you want to do?")
        print("1\t DISPLAY ALL STUDENTS")
        print("2\t DISPLAY GRADES")
        print("3\t ADD STUDENT")
        print("4\t UPDATE STUDENT")
        print("5\t DELETE STUDENT")
        print("6\t CALCULATE AVERAGE GRADE")
        print("7\t GET HIGHEST GRADE")
        print("8\t GET LOWEST GRADE")
        print("9\t GENERATE REPORT")
        print("10\t SAVE DATA")
        print("11\t EXIT")
        choice = get_user_choice()
        execute_user_choice(choice)
        print("Task Done...\n\n")


def save_students_to_file():
    data = json.dumps(students)
    with open("data.json", "w") as file:
        file.write(data)
    print("Info Saved Successfully......")


def load_students_from_file():
    with open("data.json") as file:
        content = file.read()
        if content:
            data = json.loads(content)
            global students
            students = data


def generate_report():
    """Code to generate report"""
    fieldnames = ['name', 'age', *list_of_subjects, 'grade', 'average']
    with open("report.csv", "w") as file:
        csv_writer = DictWriter(file, fieldnames)
        csv_writer.writeheader()
        for student in students:
            info = {
                "name": student["name"],
                "age": student["age"],
            }
            for subject in student["subjects"]:
                info[subject["subject_title"]] = subject["subject_score"]
            info["grade"] = student["grade"]
            info["average"] = student["average"]
            csv_writer.writerow(info)
    print("Report Generated Successfully........")


load_students_from_file()
display_menu()
