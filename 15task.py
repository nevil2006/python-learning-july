class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age,"years old.  Nice to meet you!")
s1= student("Alice", 20)
s1.greet()   