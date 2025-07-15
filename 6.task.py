# Initialize the list
my_list = [1, 2, 3, 2, 4]

# Accessing elements by index
print(my_list[0])        # Output: 1
print(my_list[1])        # Output: 2

# Modifying an element
my_list[0] = 10
print(my_list)           # Output: [10, 2, 3, 2, 4]

# Adding an element to the end
my_list.append(5)
print(my_list)           # Output: [10, 2, 3, 2, 4, 5]

# Inserting an element at a specific position
my_list.insert(1, 20)
print(my_list)           # Output: [10, 20, 2, 3, 2, 4, 5]

# Checking the length of the list
print(len(my_list))      # Output: 7

# Checking if a value exists in the list
print(5 in my_list)      # Output: True

# Removing an element (first occurrence only)
my_list.remove(5)
print(my_list)           # Output: [10, 20, 2, 3, 2, 4]

# Sorting the list in ascending order
my_list.sort()
print(my_list)           # Output: [2, 2, 3, 4, 10, 20]

# Reversing the list order
my_list.reverse()
print(my_list)           # Output: [20, 10, 4, 3, 2, 2]

# Counting how many times a value appears
print(my_list.count(2))  # Output: 2

# Final list
print(my_list)           # Output: [20, 10, 4, 3, 2, 2]

#tuple
my_tuple = (10, 20, 30, 10)

# Access
print(my_tuple[1])        # 20

# Count/Index
print(my_tuple.count(10)) # 2
print(my_tuple.index(30)) # 2

# Convert to list (to modify)
temp_list = list(my_tuple)
temp_list[0] = 99
my_tuple = tuple(temp_list)
print(my_tuple)

my_set = {1, 2, 3}

# Add
my_set.add(4)

# Remove
my_set.remove(2)           # Raises error if not found
my_set.discard(10)         # No error if not found

# Membership
print(3 in my_set)         # True

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))          # {1, 2, 3, 4, 5}
print(a.intersection(b))   # {3}
print(a.difference(b))     # {1, 2}

#dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Access
print(student["name"])        # Alice
print(student.get("score"))   # None (no error)

# Modify
student["age"] = 21
student["score"] = 95

# Remove
del student["grade"]
student.pop("score")

# Keys, Values, Items
print(student.keys())         # dict_keys(['name', 'age'])
print(student.values())       # dict_values(['Alice', 21])
print(student.items())        # dict_items([('name', 'Alice'), ('age', 21)])

# Check
print("name" in student)      # True
