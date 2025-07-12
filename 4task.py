# for and while loop
for i in range(5):
    print(i)
    print("loop",i)
    
# while loop numbers

count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    print()
#variables

count = 'a'

while count < 'h':
    print("Count is:", count)
    count = chr(ord(count) + 1)
    
    #task number
# Expected: Print only odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

#PASSOWORD
password = ""
while password != "NEVIL123":
    password = input("Enter password: ")
print("Access granted!")

#WORD COUNT
# Expected: Only names with >5 characters and containing 'a' (case-insensitive)
names = ["Alice", "JonAthAn", "Bob", "AnAstAsiA", "Sam", "Carla", "Ben"]

for name in names:
    if len(name) > 5 and 'a' in name.lower():
        print(name)
