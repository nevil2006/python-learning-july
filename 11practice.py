#Use map() and a lambda to square each number in a list of integers from 1 to 10.
numbers=list(range(1, 11))
squared=list(map(lambda x: x * x, numbers))
print(squared)
#Write a recursive function to calculate the sum of all digits in a number (e.g., 1234 → 1+2+3+4 = 10).
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
#Use reduce() to multiply all odd numbers in a list. Combine it with filter().
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda x:x %2 !=0, numbers))
products=reduce(lambda x, y: x * y, odd_numbers)
print("Sum of digits:", sum_of_digits(1234))

