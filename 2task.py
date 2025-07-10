#pratice question 1
nam=input("Enter your name:")
age=int(input("Enter you age:"))

print("Hello",nam,"you are",age,"years old.")

# pratice question 2

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
x=num1+num2
print("The sum of",num1, "and", num2, "is",x)
Y=num1-num2
print("The differnce of",num1, "and", num2 ,"is",Y)
z=num1*num2
print("The product of", num1, "and",num2, "is",z)
w=num1/num2
print("The division of",num1,"and",num2,"is",w)

#quiz
first_one = input("Who is the Prime Minister of India: ")
second_one = input("When did India get independence: ")

if first_one.lower() == "modi" and second_one == "1947":
    print("2 points")
elif first_one.lower() == "modi" or second_one != "1947":
    print("1 point")
elif first_one.lower() != "modi" and second_one == "1947":
    print("1 point")
else:
    print("Try again")
