import os
p = (1,2) + (3,4)
q = (1,2,5)*5
print(p, q)
myfile = open('myfile.txt','w')
myfile.write('Hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
print(myfile.read())
myfile.close()
print(os.getcwd())
print(os.listdir())
