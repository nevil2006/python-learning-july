#beginner
classrooms = {
    "classroom A": {
        "Student 1": {"name": "Alice"},
        "student 2": {"name": "NEVIL"}
    },
    "classroom B": {
        "Student 1": {"name": "Charlie"},
        "Student 2": {"name": "Diana"}  
    }
}

print("Second student in first class:", classrooms["classroom A"]["student 2"]["name"])
#intermediate
# Nested dictionary of students
students = {
    "Classroom A": {
        "Alice": {"age": 12, "grade": "6th"},
        "Bob": {"age": 13, "grade": "7th"}
    },
    "Classroom B": {
        "Charlie": {"age": 14, "grade": "8th"},
        "Diana": {"age": 12, "grade": "6th"}
    }
}

# User input to search for student
# Nested dictionary of students
students = {
    "Classroom A": {
        "Alice": {"age": 12, "grade": "6th"},
        "Bob": {"age": 13, "grade": "7th"}
    },
    "Classroom B": {
        "Charlie": {"age": 14, "grade": "8th"},
        "Diana": {"age": 12, "grade": "6th"}
    }
}

# User input to search for student
search_name = input("Enter student name to search: ")

found = False

try:
    for classroom in students:
        if search_name in students[classroom]:
            info = students[classroom][search_name]
            print(f"{search_name} found in {classroom}: Age {info['age']}, Grade {info['grade']}")
            found = True
            break
    if not found:
        raise ValueError("Student not found.")
except Exception as e:
    print("Oops! Something went wrong:", e)


