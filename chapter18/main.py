# def func(a, b , c =5):
#     print(a,b,c)
# func(1,c = 3 ,b =2)

# def func(a, **args):
#     print(a,args)

# func(a=1,b = 23,c =45)

def func(a,b,c = 3, d=4): print(a,b,c,d)

func(1,*(5,6))