L = [lambda x : x*2,lambda x : x**2, lambda x : x//2]
for f in L:
    print(f(5))
print(L[1](5))

print(list(filter(lambda x : x > 0, range(-5,5))))