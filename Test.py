""" text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''


splited_text = text.split()
text = text.replace('.','')
search_word = input('Search: ')

position = 0
s
for position, word in enumerate(text):
    if search_word == word:
        print('Search word: ', search_word)
        print('Position: ', position+1)
        break
else: 
    print('Search word: ', search_word)
    print('No such word: ', position)
 """

 