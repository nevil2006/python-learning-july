#Divide Two Numbers with Error Handling
try:
    num1 = float(input("Enter the first number: ")) 
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print("Result:", result)
#Create a calculator program that takes two numbers and an operator (+, –, *, /), handles wrong inputs and invalid operations using exceptions.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Please use +, -, *, or /.")

    print("Result:", result)

except ValueError as ve:
    print("Error:", ve)
except ZeroDivisionError as ze:
    print("Error:", ze)
finally:
    print("Calculation completed.")
