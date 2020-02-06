# Now, we will work once again with these two strings:
# string01 = 'Bratislava'
# string02 = 'Budapest'
#
# Write a script that will find and print only the elements using a suitable
# operator or method:
#
# 1. Difference - which string01 and string02 do not share.
#    In other words, the elements that are located in string01, string02,
#    but not in both.
# 2. All - which string01 and string02 share and which they do not share -
#    all elements.

string01 = 'Bratislava'
string02 = 'Budapest'

print(f'Different characters: {set(string01).symmetric_difference(set(string02))}')
print(f'All characters: {set(string01).union(set(string02))}')

