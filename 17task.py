class animal:
    def speak(self):
        print("animal speaks")
class dog (animal):
    def speak(self):
        print("dog barks")
        
class Person:                   
    def __init__(self, name):
        self.name = name

class Student(Person):       
    def __init__(self, name, roll):
        super().__init__(name)  
        self.roll = roll
class Bird:               # 👉 Parent
    def sound(self):
        print("Chirp")

class Parrot(Bird):       # 👉 Child
    def sound(self):
        print("Squawk")
from abc import ABC, abstractmethod

class Vehicle(ABC):       # 👉 Abstract Parent class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):       # 👉 Child class (implements abstract method)
    def start(self):
        print("Car started")
class Shape:              # 👉 Parent
    def draw(self):
        print("Drawing shape")

class Circle(Shape):      # 👉 Child
    def draw(self):       # Overrides parent method
        print("Drawing circle")

