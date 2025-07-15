# welcome using function
def welcome(name):
    print("welcome", name)
welcome("Nevil")
#Write a function is_even(n) that returns True if the number is even, False otherwise.
def is_even(n):
    if n % 2 == 0:
        print("true")
        return True
    else:
        print("false")
        return False

n = int(input("Enter a number: "))
is_even(n)
# calculator
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"
print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '-'))  # Output: 5
print(calculator(10, 5, '*'))  # Output: 50
print(calculator(10, 5, '/'))  # Output: 2.0
print(calculator(10, 0, '/'))  # Output: Error: Division by zero
print(calculator(10, 5, '%'))  # Output: Invalid operator
