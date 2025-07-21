#Given two lists of names and scores, use zip() to create a dictionary of name:score pairs.
names= ["alice", "bob", "charlie"]
scores = [81, 92, 56]
scored=dict(zip(names,scores))
print(scored)
#Loop over a list using enumerate() and print only items at even indices.
vegetables = ["carrot", "broccoli", "spinach", "cauliflower"]
for idx,val in enumerate(vegetables):
    if idx%2==0:
        print(idx, val)
#Sort a list of tuples (name, score) based on scores in descending order using sorted() with key=.
# Sample list of (name, score) tuples
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 90)]

# Sort by score in descending order
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

# Print the sorted list
print(sorted_students)


