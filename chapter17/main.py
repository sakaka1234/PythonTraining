X = 99
def func(Y):
    return X + Y

print(func(1))

X = 'Hack'
def func():
    X = 'Py'
    def nested():
        nonlocal X
        X = 'HACK'
    nested()
func()
print(X)