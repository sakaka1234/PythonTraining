class tracer: 
    def __init__(self,func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args)

@tracer
def hack(a,b,c):
    return a + b + c 

if __name__ == '__main__':
    print(hack(1,2,3))
    print(hack('a','b','c'))