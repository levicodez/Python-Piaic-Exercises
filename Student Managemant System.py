def manage_student_database() -> None:
    student_data: list = []
    names: list[str] = []
    ids: list[str] = []
    counter: int = 1
    student_name: str = ""

    while (student_name != "stop"):
        student_name = input("Enter a name : ")

        if (student_name in names):
            print("Name is already in the list")

        if (student_name != "stop" and student_name not in names and student_name != ""):
            names.append(student_name)
            ids.append(counter)
            counter += 1
    student_data = list(zip(ids, names))
    print(f"\nComplete list of students :\n{student_data}")
    print("\nList of Student with Ids : ")

    for student_info in student_data:
        print(f"ID: {student_info[0]}, Name: {student_info[1].title()}")

    print(f"\nTotal number of students : {len(names)}")

    print(f"Total length of all student names combined: {len("".join(names))}")

    print(f"The student with the longest name is: {max(names, key=len)}")

    print(f"The student with the shortest name is: {min(names, key=len)}")
    # print(names)


manage_student_database()
