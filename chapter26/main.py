class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

class Car:
    pass
class Person:
    def say_name(self):
        print("My object is", self)

p = Person()
p.say_name()
print(Car)

c1 = Car()
print(c1)
d = Dog()
d.speak()