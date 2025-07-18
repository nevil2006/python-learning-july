#for loop
name =["madhan","perusu","mama"]
for studnets in name:
    print(studnets)
#while loop
student_count = 190

while student_count > 0:
    student_count -= 62
    if student_count > 0:
        print("Student count is:", student_count)

print("No more students left.")
#break
for i in range(1,10):
    if i==5:
        break
    print(i)
#continue
for i in range(1,10):
    if i==5:
        continue
    print(i)
#range type1
for i in range(5):
    print(i)
#range type2
for i in range(1,5):
    print(i)
#range type3
for i in range(1,10,1):
    print(i)
#even number
for i in range(1, 10, 1):
    if i % 2 == 0:
        print(i)
    else:
        continue  
#set
set1 = {1, 2, 3, 4}
set2 = {5, 6}
set3 = {7, 5, 1, 10}

temp = set1.union(set2)             
result = temp.intersection(set3)
print(result)

#list initiliaze
i = []  

for num in range(2, 120, 2):
    i.append(num)         
    print("Added:", num) 

print("Final List:", i)   
# list comprehension
arr = [1, 2, 3, 4, 5, 6]
odd = []
even = []

for i in arr:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

print("Odd numbers:", odd)
print("Even numbers:", even)
#dictionary comprehension
cities=["mumbai","newyork","moscow"]
countries=["india","usa","russia"]
z=zip(cities,countries)
for a in (z):
    print(a)
d = {city: country for city, country in zip(cities, countries)}
print(d)
#enumerate
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print("Index:", index, "| Fruit:", fruit)            