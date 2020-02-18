'''
Write a program that will take a list of words as input and will print to the terminal the longest word and its
length in one tuple.
'''

words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

long_word = 0

while words:
    word = words.pop(0)
    if len(long_word) <= len(word):
        long_word = word
    else: continue

print(long_word)
