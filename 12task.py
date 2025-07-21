#zip():
name=["alice", "bob", "charlie"]
score=[81,92,56]
zipped=list(zip(name,score))
print(zipped)
#enumerate():
vegetables=["carrot", "broccoli", "spinach","califlower"]
for idx, val in enumerate(vegetables):
    print( idx, " ", val)
#all():
marks=[90, 85, 78, 92]
print(all(m > 50 for m in marks))  
print(any(m > 60 for m in marks))  
#sorted():
fruits=["banana", "apple", "cherry", "date"]
print(sorted(fruits,key=len))
#list comprehension:
squared = [x*x for x in range(1,11)]
print(squared)
