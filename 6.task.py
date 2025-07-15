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
