num_rep = int(input('Number of repetition: '))
sentence = input('Enter sentence: ')

output = ''

words = list(sentence.split())

while words:
    word = words.pop(0)
    output = output + ((word + ' ') * num_rep)

print(output)