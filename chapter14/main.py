for x in [1,2,3,4]: print(x**2,end=' ')
print(open('data.txt').read())
f = open('data.txt')
f.readline()
print(f)
for line in open('data.txt').readlines():
    print(line.upper(), end=' ')
L = [1,2]
I = iter(L)
next(I)
print(I)
L = [1,2,3,4,5]
L = [x + 10 for x in L]
print(list(L))
f = open('data.txt')
lines = f.readlines()
print(list(lines))
lines = [line.rstrip() for line in lines]
print(list(lines))