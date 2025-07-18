#1
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print("Squares of even numbers:", squares)
#2
names = ['Ram', 'Sam']
scores = [85, 92]
result = {name: score for name, score in zip(names, scores)}
print("Student scores:", result)
#3
fruits = ["apple", "banana", "grape", "avocado", "mango"]
for fruit in fruits:
    if fruit.startswith("a"):
        continue
    print(fruit)
#4
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
