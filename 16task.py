# __init__() Method 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("John", 20)
print(s1.name)
print(s1.age)

# self Keyword 
class Car:
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print("Model:", self.model)

c1 = Car("Tesla")
c1.show_model()

# Encapsulation
class Account:
    def __init__(self):
        self._balance = 1000  # protected
        self.__pin = 1234     # private

a = Account()
print(a._balance)       # ✅ Accessible (protected)
# print(a.__pin)        # ❌ Uncommenting will raise AttributeError

# Public vs Private vs Protected
class Test:
    def __init__(self):
        self.name = "Public"
        self._age = 20
        self.__secret = "Hidden"

t = Test()
print(t.name)           # ✅ Public
print(t._age)           # ⚠️ Protected (should be used carefully)
# print(t.__secret)     # ❌ Will raise error (private)

# Creating Multiple Objects
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")
print(dog1.name)        # Buddy
print(dog2.name)        # Charlie

# Modifying Object Properties
class Person:
    def __init__(self, name):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

p = Person("John")
p.set_name("Mike")
print(p.name)           # Mike

# Class vs Instance Variables
class Employee:
    company = "Google"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")
print(e1.company)       # Google (from class)
print(e2.name)          # Bob (instance)
