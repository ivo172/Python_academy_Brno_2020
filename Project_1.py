TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

users = {'bob': 123, 'ann': 'pass123', 'mike': 'password123', 'liz': 123}

print(80 * '-')  # Print line
print('Welcome to the app. Please log in:')
username = input('USER: ')

ok_pass = str(users.get(username, 'wrong'))

if ok_pass == 'wrong':  # Validation username, if username isn't in USERS ==> None
    print('Username not found!')
    quit()

password = str(input('PASSWORD: '))

if password != ok_pass:  # Validation password
    print('Password is wrong!')
    quit()

print(80 * '-')  # Print line

choice_text = input('We have 3 texts to be analyzed. '
                    'Enter a number btw. 1 and 3 to select: ')
print(80 * '-')  # Print line

text = TEXTS[(int(choice_text)) - 1]  # =>int
# 1, 2 and 3 is in list, therefore -1

text = text.replace(',','').replace('.','')

print(f'Select text: \n{text}')
print(80 * '-')  # Print line

words = (str.split(text))

print(f'There are {len(words)} words in the selected text.')

title_word = []

for word in words:  # Test first character in word
    if word[0].isupper():
        title_word += '1'
print(f'There are {len(title_word)} titlecase words.')

upper_word = []

for word in words:
    if word.isupper():
        upper_word += '1'
print(f'There are {len(upper_word)} uppercase words.')

lower_word = []

for word in words:
    if word.islower():
        lower_word += '1'
print(f'There are {len(lower_word)} lowercase words.')

numeric_word = []
suma_num_word = 0

for word in words:
    if word.isnumeric():
        suma_num_word = suma_num_word + int(word) # Count numeric word in text
        numeric_word += '1'
print(f'There are {len(numeric_word)} numeric string.')
print(80 * '-')  # Print line

count_char = []

for word in words:  # Count character in word and added in count_char.
    count_char.append(len(word))

characters = {}
count_char = sorted(count_char)  # Sorted number in list count_char

while count_char:
    char = count_char.pop(0)                        # from list to dict.
    characters[char] = characters.get(char, 0) + 1

for x, y in characters.items():
    print(f'{x:>2} {y * "*"} {y}')  # Print from dictionary, x = key, y = value

print(80 * '-')  # Print line
print(f'If we summed all the numbers in this text we would get: {suma_num_word}')
print(80 * '-')  # Print line