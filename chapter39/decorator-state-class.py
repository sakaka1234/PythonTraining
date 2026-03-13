class tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwds):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args,**kwds)

@tracer
def hack(a, b, c): # Same as: hack = tracer(hack)
    print(a + b + c) # Triggers tracer.__init__
@tracer
def code(x, y): # Same as: code = tracer(code)
    print(x ** y) # Wraps code in a tracer object
if __name__ == '__main__':
    hack(1, 2, 3) # Really calls tracer instance: runs tracer.__call__
    hack(a=4, b=5, c=6) # hack is an instance attribute
    code(4, 2) # Really calls tracer instance: self.func is code
    code(2, y=16) # self.calls is per-decoration here