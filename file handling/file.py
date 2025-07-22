# operations open,read,close
file=open(r'C:\Users\nevil\Desktop\python-learning-july\file handling\info.txt','r')
print(file.read())
file.close()
#read line
print(file.readline())

file.close()    
#write
file=open(r'C:\Users\nevil\Desktop\python-learning-july\file handling\info.txt','w')
file.write('This is a new line added to the file.')
file.close()
#append
file=open(r'C:\Users\nevil\Desktop\python-learning-july\file handling\info.txt','a')

file.write('This line is appended to the file.')
lst=['hi hi hi',"welcome to code.io"]
file.writelines()
file.close()
