"""
Construct a student class and heapify based on the maximum marks obtained.
"""

import heapq as pq


class Student:
    def __init__(self, name: str, age: int, marks: float):
        self.name = name
        self.age = age
        self.marks = marks

    def print(self):
        print(self.name+" "+str(self.age)+" "+str(self.marks))

    def __lt__(self, obj: object) -> bool:
        if self.marks != obj.marks:
            return self.marks > obj.marks
        else:
            return self.age < obj.age

    def __eq__(self, __o: object) -> bool:
        return self.marks == __o.marks and self.age == __o.age


students = []
students.append(Student("Soham", 24, 92))
students.append(Student("Raj", 25, 92))
students.append(Student("Annand", 25, 88))
students.append(Student("Rohan", 25, 36))
pq.heapify(students)
n = len(students)
for i in range(n):
    student = pq.heappop(students)
    student.print()