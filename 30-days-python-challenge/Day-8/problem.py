
#Q1:Create a Student class that stores:
#- name
#- age
#- course
#Then create two student objects and display their details.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


s1 = Student("Rame", 39, "Python")

print(s1.name)