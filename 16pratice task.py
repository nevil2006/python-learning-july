#Create a BankAccount class
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
#Laptop Class
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")
        print(f"Price: ₹{self.price}")
#Build a Student class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # assume it's a dictionary: {'Math': 90, 'Science': 80}

    def calculate_grade(self):
        total = sum(self.marks.values())
        avg = total / len(self.marks)

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(f"{self.name}'s Grade: {grade}")
