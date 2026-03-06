from animals import Dog
from student import Student
from number import Number
d = Dog()
d.bark()

print(Student.school)

s1 = Student("Sa",12)
print(s1.school)

s = Student("Anna", 20)

print(s.name)
print(s.age)

a = Number(10)
b = Number(5)

c = a + b 

print(c.value)