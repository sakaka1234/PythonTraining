string = 'TEXT'
a, b, c , d = string
print(a,b,c,d)
L = [1,2,3,4,5,6]
while L:
    front , L = L[0] , L[1:]
    print(front,L)
seq = [1,5,6,7,8,9,132]
a , *b = seq
print(b)
*c, d = seq
print(c)
a, *b , c = seq
print(b)
a = b = c = 'code'
print(a,b, sep=', ')