text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

text = text.replace(',','').replace('.','')
splited_text = text.split()
search_word = input('Search: ')

position = 0

for position, word in enumerate(splited_text):
    if search_word == word:
        print('Search word: ', search_word)
        print('Position: ', position+1)
        break
else:
    print('Search word: ', search_word)
    print('No such word: ', search_word)



data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]

total_price = 0.0

for list_ in range(1, len(data)):
    for index, item in enumerate(data[list_]):
        if index == 2:
            total_price = total_price + item

print(total_price)

