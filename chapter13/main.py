L1 = [1,2,3,4]
L2 = [5,6,7,8]
print(zip(L1,L2))
print(list(zip(L1,L2)))
i = -1 
while (i := i + 1) < len(L1):
    print(f'{L1[i]} + {L2[i]} = {L1[i] + L2[i]}')
a = list(zip(range(4), 'hack'))
print(a)
T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
a = list(zip(T1,T2,T3))
print(a)
S = 'hack'
a = [k*i for (i,k) in enumerate(S)]
print(a)