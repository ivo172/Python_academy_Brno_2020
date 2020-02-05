'''
5. Calculate the following statistics for the selected text:
    number of words in total
    number of words starting with capital letter
    number of uppercase words
    number of lowercase words
    number of numeric-only words (e.g. 100, not 100N)

6. Create a bar chart depicting the frequencies of word lengths in the text. For example:

    1 * 1
    2 *********** 11
    3 *************** 15
    4 ********* 9
    5 ********** 10

    In the above chart, there is one word of length 1, 11 words of length 2, 15 words of length 3 etc.

7. Calculate the sum of all the numeric "words" in the given text. For example the sum for the string below would be 8500:
    "that rises sharply some 1000 feet above
    Twin Creek Valley to an elevation of more
    than 7500 feet above sea level. The butte
    is located just north of US 30N"

----------------------------------------
Welcome to the app. Please log in:
USERNAME: bob
PASSWORD: 123
----------------------------------------
We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: 2
----------------------------------------
There are 62 words in the selected text.
There are 10 titlecase words
There are 0 uppercase words
There are 51 lowercase words
There are 1 numeric strings
----------------------------------------
 2 ******* 7
 3 ***************** 17
 4 ********* 9
 5 ********** 10
 6 ******* 7
 7 *** 3
 8 ** 2
 9 ***** 5
10 * 1
13 * 1
----------------------------------------
If we summed all the numbers in this text we would get: 300.0
----------------------------------------
'''
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
users = {'bob':123, 'ann':'pass123', 'mike':'password123', 'liz':123}

print(80 * '-') # Print line
print('Welcome to the app. Please log in:')
username = input('USER: ')

ok_pass = str(users.get(username, 'wrong'))

if ok_pass == 'wrong':     # Validation username, if username isn't in USERS ==> None
    print('Username not found!')
    quit()

password = str(input('PASSWORD: '))

if password == ok_pass:     # Validation password
    pass
else:
    print('Password is wrong!')
    quit()
print(80 * '-') # Print line

choice_text = input('We have 3 texts to be analyzed. '
                    'Enter a number btw. 1 and 3 to select: ')
print(80 * '-') # Print line

text = TEXTS[(int(choice_text)) - 1]    # =>int
                                        # 1, 2 and 3 is in list, therefore -1
print(f'Your selection is this text: \n{text}')
print(80 * '-') # Print line





