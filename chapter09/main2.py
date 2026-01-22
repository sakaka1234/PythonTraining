X, Y ,Z = 62, 63, 64
S = 'Text'
D = {'a': 1, 'b': 2}
L = [1,2,3]
F = open('datafile.txt','w')
F.write(S + '\n')
F.write(f'{X}, {Y}, {Z}\n')
F.write(str(L) + '$' + str(D) + '\n')
chars = open('datafile.txt').read()
print(chars)
F.close()