'''
Write a Python program that will create "echo sentences". Each word in the sentence we will feed in, should be repeated n number of times. The number of repetitions and the sentence to be manipulated are inputs provided by the user.

Example:
If the supplied number of repetitions is 3 and the sentence: 'I do not want to work today'.

Output:
'I I I do do do not not not want want want to to to work work work today today today'

The resulting sentence cannot begin with space, unless the input sentence contained it.
'''

num_rep = int(input('Number of repetition: '))
sentence = input('Enter sentence: ')

output = ''

<<<<<<< HEAD
sentence.split()
=======
words = list(sentence.split())
>>>>>>> 87855e7e75b28d8b41fa8b9f6ee737ccdf23fccf

while words:
    word = words.pop(0)
    output = output + ((word + ' ') * num_rep)

print(output)