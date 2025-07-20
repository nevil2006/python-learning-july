#lambda
square = lambda x: x * x
print(square(20))  
#syntax of lambda function
#lambda argumensts:expression#
# map
numbers=[1,2,3,6]
sqaured=list(map(lambda x: x * x,numbers))
print(sqaured)
# filter
nums=[5,12,10,16,15,20,19]
even=list(filter(lambda x: x % 5 == 0, nums))
print(even)
#reduce
from functools import reduce
nums = [1, 2, 3, 5]
product = reduce(lambda x, y: x * y, nums)
print(product) 
#recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

