"""
Our task is to extract an overview of what unique names
and surnames do we have in the class.
"""
from typing import Any, Union

students = ['Adam, Baker', 'Chelsea, Archer',
            'Marcus, Archer', 'Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker', 'Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman', 'Abraham, Mason',
            'Marcus, Sawyer', 'Alex, Glover',
            'Glenn, Cook', 'Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater', 'Alex, Mason',
            'Tyler, Fisher', 'Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']


student = ()
names = []


while students:
    student = students.pop(0)
    names = student.split()
    print(names)

