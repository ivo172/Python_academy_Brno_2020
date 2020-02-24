names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal'
        ]

sorted_names = [names.pop(0)]

for name in names:

    for i,s_name in enumerate(sorted_names):
        if name < s_name:
            sorted_names.insert(i,name)
            break
    else:
        sorted_names.append(name)

print(sorted_names)