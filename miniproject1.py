students = []

# ✅ Add Student (takes input inside the function, no need for parameters)
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    
    students.append(student)
    print(f" Student '{name}' added successfully.\n")

# ✅ View Students (you named it `display_students`, but used `view_students()`, so we rename it)
def view_students():
    if not students:
        print(" No students found.\n")
    else:
        print("\n All Students:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        print()

# ✅ Search student by name
def search_student():
    search_name = input(" Enter student name to search: ")

    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f" Found: Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")

# ✅ Delete student by name
def delete_student():
    delete_name = input(" Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print(" Student deleted successfully!\n")
            return

    print(" Student not found. Nothing deleted.\n")

# ✅ Main Program Loop
while True:
    print(" Student Information System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
