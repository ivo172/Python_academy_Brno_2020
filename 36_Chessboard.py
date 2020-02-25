length = int(input('Enter length of board\'s edge:'))
char = input('Enter character: ')

for number in range(length):
    print(f'{char * (length)}')
