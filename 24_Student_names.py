
"""
Our task is to extract an overview of what unique names
and surnames do we have in the class.
"""

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


names = set()
surnames = set()

while students:
    full_name = students.pop()
    name, surname = full_name.split(',')
    names.add(name)
    surnames.add(surname)

print(f'Unique names: {names}')
print(f'Unique surnames: {surnames}')
