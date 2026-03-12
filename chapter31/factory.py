def factory(aClass, *pargs, **kargs):        
    return aClass(*pargs, **kargs)           
class Hack:
    def doit(self, message):
        print(message)
class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job  = job
object1 = factory(Hack)                      
object2 = factory(Person, 'Sue', 'dev')      
object3 = factory(Person, name='Bob')  