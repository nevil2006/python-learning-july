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