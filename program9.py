student_names = []
student_marks = []

while True:
    print("-" * 2)
    print("     STUDENT MARKS MANAGEMENT SYSTEM")
    print("-" * 2)
    print("1. Insert Student Record")
    print("2. Delete Student Record")
    print("3. Update Student Marks")
    print("4. Traverse / Display All Records")
    print("5. Search Student")
    print("6. Show Statistics")
    print("7. Exit")
    print("-" * 2)

    choice = input("Enter your choice (1-7): ").strip()

    # ---------------- INSERTION ----------------
    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in student_names:
            print(f"Student '{name}' already exists! Use update option instead.\n")
        else:
            try:
                marks = float(input(f"Enter marks for {name}: "))

                if marks < 0 or marks > 50:
                    print("Marks must be between 0 and 50.\n")
                else:
                    student_names.append(name)
                    student_marks.append(marks)

                    print(f"Record for '{name}' inserted successfully.\n")

            except ValueError:
                print("Invalid marks! Please enter a number.\n")

    # ---------------- DELETION ----------------
    elif choice == "2":
        name = input("Enter student name to delete: ").strip()

        if name in student_names:
            index = student_names.index(name)

            student_names.pop(index)
            student_marks.pop(index)

            print(f"Record for '{name}' deleted successfully.\n")
        else:
            print(f"Student '{name}' not found.\n")

    # ---------------- UPDATE ----------------
    elif choice == "3":
        name = input("Enter student name to update: ").strip()

        if name in student_names:
            index = student_names.index(name)

            try:
                new_marks = float(input(f"Enter new marks for {name}: "))

                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100.\n")
                else:
                    student_marks[index] = new_marks
                    print(f"Marks for '{name}' updated successfully.\n")

            except ValueError:
                print("Invalid marks! Please enter a number.\n")
        else:
            print(f"Student '{name}' not found.\n")

    # ---------------- TRAVERSE / DISPLAY ----------------
    elif choice == "4":
        if len(student_names) == 0:
            print("No student records available.\n")
        else:
            print("\n" + "-" * 2)
            print("        ALL STUDENT RECORDS")
            print("-" * 2)

            for i in range(len(student_names)):
                print(
                    f"{i + 1}. {student_names[i]} : "
                    f"{student_marks[i]:.2f}"
                )

            print("-" * 2 + "\n")

    # ---------------- SEARCH ----------------
    elif choice == "5":
        name = input("Enter student name to search: ").strip()

        if name in student_names:
            index = student_names.index(name)

            print(f"\nStudent found!")
            print(f"Name  : {student_names[index]}")
            print(f"Marks : {student_marks[index]:.2f}\n")
        else:
            print(f"Student '{name}' not found.\n")

    # ---------------- STATISTICS ----------------
    elif choice == "6":
        if len(student_marks) == 0:
            print("No records available to calculate statistics.\n")
        else:
            highest = max(student_marks)
            lowest = min(student_marks)
            average = sum(student_marks) / len(student_marks)

            highest_index = student_marks.index(highest)
            lowest_index = student_marks.index(lowest)

            print("\n" + "-" * 2)
            print("           STATISTICS")
            print("-" * 2)
            print(f"Total students : {len(student_names)}")
            print(f"Average marks  : {average:.2f}")
            print(
                f"Highest marks  : {highest:.2f} "
                f"({student_names[highest_index]})"
            )
            print(
                f"Lowest marks   : {lowest:.2f} "
                f"({student_names[lowest_index]})"
            )
            print("-" * 2 + "\n")

    # ---------------- EXIT ----------------
    elif choice == "7":
        print("Exiting Student Marks Management System...")
        print("Thank you!")
        break

    # ---------------- INVALID CHOICE ----------------
    else:
        print("Invalid choice! Please enter a number from 1 to 7.\n")