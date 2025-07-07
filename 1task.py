# Variable types
a = 10        # int
b = 3.14      # float
name = "Sara" # str
is_ready = True  # bool

# Type casting
print(int("5") + 2)        # Converts string to int → 7
print(float("2.5") + 1.5)  # Converts to float → 4.0
print(str(100) + " apples")  # Converts to str → "100 apples"

name = input("Enter your name: ")
age = input("Enter your age: ")
fav_number = input("Enter your favorite number: ")

print(f"Hi {name}, you're {age} years old and your favorite number is {fav_number}.")

num = 10
text = "20"

# Wrong: print(num + text) → TypeError
print(num + int(text))      # 30
print(str(num) + text)      # "1020"

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

