student={}

while True:
    print("\n----STUDENT MANAGER APP-----")
    print("1.Add Student")
    print("2.View Student")
    print("3.Check Result")
    print("4.Delete student")
    print("5.Exit")

    choice = input("Enter your choice:")

    #Add student(Create)
    if choice =="1":
        name = input("Enter student name:")
        marks = int(input("Enter marks:"))
        student[name] = marks
        print(f"{name} Successfully Added!!")


    #View student
    elif choice =="2":
        if not student:
            print("No Studnet found!")
        else:
            for name,marks in student.items():
                print(name,":",marks)


    #check result
    elif choice =="3":
        name = input("Enter student name:")

        if name in student:
            marks = student[name]

            if marks >= 50:
                print("PASS")
            else:
                print("FAIL")

        else:
            print(" Student Not found ")  


    #Delete student
    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in student:
            del student[name]
            print("Updated Students:", student)
        else:
            print("Student not found")

    # Exit
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid input")