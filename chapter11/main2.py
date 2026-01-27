print()
x = 'python'
y = 3.12
z = ['lp6e']
print(x,y,z)
print(x,y,z ,sep='...\n')
print(x,y,z,sep='...',file=open('data.txt','w'))
text = '%s: %-.4f, %05d' % (x, y, int(z[0][-2]))
print(text)