class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):  # Overriding
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

# Example usage
emp = Employee("Alice", 30, "EMP123")
emp.display()
