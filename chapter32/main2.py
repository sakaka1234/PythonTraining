class AgeDesc:
    def __get__(self, instance, owner):
        return 40
    def __set__(self, instance, value):
        instance._age = value

class WithDescriptors:
    age = AgeDesc()

x = WithDescriptors()
print(x.age)