print(len([1,2,3]))
print([1,2,3] + [4,5,6])
print(str([1,2]) + '34')
#index and slide assignments
L = ['code', 'Code' , 'CODE!']
L[1] = 'Hack'
L[0:2] = ['write','Python']
print(L)
A = [1,2,3]
A[1:2] = [4,5]
print(A)
A[:0] = [2,3,5]
print(A)