#Create a class Book with attributes title, author, and pages, and a method description() that prints these details.
class Book:
    def __init__(self, title, author, pages):
        self.title = title       
        self.author = author     
        self.pages = pages

    def description(self):      
        print("Title:", self.title)
        print("Author:", self.author)
        print("page:",self.pages)
s1= Book("2006","nevil",150)
s1.description()
#Define a class Rectangle with a method to calculate area and perimeter
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length +self.width)
r1=Rectangle(5,10)
print(r1.area())
print(r1.perimeter())
#Make a class BankAccount with deposit and withdraw methods and a private balance attribute.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
    def withdraw(self, amount):
        if amount>0 and amount<=self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")   
a1 = BankAccount(100)
a1.deposit(50)
a1.withdraw(20)
a1.withdraw(200)  