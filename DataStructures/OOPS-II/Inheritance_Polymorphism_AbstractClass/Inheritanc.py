"""
Write a python code that defines a parent class Person and a child class Student. The person class
has attributes for a person's name and age, and a display method to print these attributes.
The Student class inherits from the Person class and adds a new attribute for the student's
date of birth(dob) and a display info method to print all three attributes (name, age and dob).
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, dob):
        super().__init__(name, age)
        self.dob = dob

    def display_info(self):
        print(self.name, self.age, self.dob)


obj = Student("Rahul", 23, "16-03-2000")
obj.display()
obj.display_info()