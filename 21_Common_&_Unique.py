# Write a script that will find and print only elements using a suitable operator or method:
# # Common - which have string01 and string02 common.
# Unique - which characters are present in string01 but not in string02.

string01 = 'Bratislava'
string02 = 'Budapest'

common = set(string01) & set(string02)
unique = set(string01) - set(string02)

print(f'Common characters: {list(common)}')
print(f'Unique characters: {list(unique)}')
