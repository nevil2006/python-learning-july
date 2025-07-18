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
