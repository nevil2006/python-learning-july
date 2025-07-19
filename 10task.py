#functions

def greet():
    print("hello")
    print("good morning")
    
greet()

def add(x,y):
    c=x+y
    print(c)
add(10,15)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)
#parameter
def add(a, b):
    return a + b

add(2, 3)  # 2 is assigned to a, 3 to b
#Default Arguments
def greet(name, message="Hello"):
    print(message, name)

greet("Alice")         # Uses default: Hello Alice
greet("Bob", "Hi")     # Overrides default: Hi Bob
# *args	**kwargs
def order_summary(*items, **details):
    print("Items ordered:", items)
    print("Extra details:", details)

order_summary("Pizza", "Burger", table=5, waiter="John")
#function types
#local scope
def greet():
    name = "Alice"
    print(name)

greet()       # Alice
# global scope
x = 5

def change():
    global x
    x = 10

change()
print(x)  # 10
#with return
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7
#without return
def hello():
    print("Hi")

x = hello()     # Hi
print(x)        # None
