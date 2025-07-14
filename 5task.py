# welcome using function
def welcome(name):
    print("welcome", name)
welcome("Nevil")
#Write a function is_even(n) that returns True if the number is even, False otherwise.
def is_even(n):
    if n % 2 == 0:
        print("true")
        return True
    else:
        print("false")
        return False

n = int(input("Enter a number: "))
is_even(n)
