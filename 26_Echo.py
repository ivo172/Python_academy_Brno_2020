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

output = []

sentence.split()

print(sentence)

for word in sentence:
    output.append(num_rep * word)
    

print(output)