from PyQt5 import QtWidgets
app = QtWidgets.QApplication([])

# Hlavní okno
main = QtWidgets.QWidget()
main.setWindowTitle('Hello Qt')

# Layout pro hlavní okno
layout = QtWidgets.QHBoxLayout()
main.setLayout(layout)

# Nápis
label = QtWidgets.QLabel('Click the button to change me')
# Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
layout.addWidget(label)

# Tlačítko
button = QtWidgets.QPushButton('Click me')
layout.addWidget(button)

# Funkcionalita
def change_label():
    label.setText('Good job. +100 points.')

button.clicked.connect(change_label)

# Spuštění
main.show()
app.exec()



# import json
#
# d = {'X12345': {'ID': 'X12345', 'full_name': 'Jack Frank', 'birthdate': '1.1.1970', 'job_title': 'welder', 'position_from': '1.5.2015', 'contract_start': '1.2.2013', 'contract_end': '31.12.2020',
#                'salary': 123456}, 'X54321':  { 'ID': 'X54321', 'full_name': 'Bob Doe', 'birthdate': '8.8.1971', 'job_title': 'machinist',
#                 'position_from': '1.8.2016', 'contract_start': '1.8.2014', 'contract_end': '31.12.2021',
#                 'salary': 23451}}
#
# json.loads(d.replace("'", '"'))
#
# print(type(d))
# print(d)





# def fuunction(a, b, *args, default=None, **kwargs):
#     print(a, b, args, default, kwargs)

# function(1, 2, 3, 4, 5, 6, )




# my_string = 'New York'
#
# for char in reversed(my_string):
#     print(char, end='')
#
#
#

# def convert_height(inches):
#     return inches * 0.025
#
#
# def convert_weight(pounds):
#     return pounds * 0.45
#
#
# def calculate_bmi(pounds, inches):
#     kilograms = convert_weight(pounds)
#     meters = convert_height(inches)
#     bmi = kilograms / meters**2
#     return bmi
#
#
# print(calculate_bmi(185, 89))



# def division(x,y):
#     if y != 0:
#         return x/y
#
# print(division(8,4))





# words =['bbc', 'def', 'klm', 'kla']
# word_a = words.pop(0)
#
# print(word_a)
#
# for word in words:
#     if word > word_a:
#         word_a = word_a + word
#
# print(word_a)



# text = '''
# Situated about 10 miles west of Kemmerer,
# Fossil Butte is a ruggedly impressive
# topographic feature that rises sharply
# some 1000 feet above Twin Creek Valley
# to an elevation of more than 7500 feet
# above sea level. The butte is located just
# north of US 30N and the Union Pacific Railroad,
# which traverse the valley.'''

# text = text.strip(',./+-:!?')
# split_text = text.split()

# position = 0
# index = 0
# found = False

# search_word = input('Search word: ')
# for index, word in enumerate(split_text):
#     if word == search_word:
#         position = index + 1
#         found = True
#         print(str(position))
        
# if not found:
#     print('No such word')






# data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
#         ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
#         ['534','Paralen', 19.90, 3229, 'Zentiva'],
#         ['327','Smecta', 68.00, 2709, 'Sipsen'],
#         ['242','Uniclophen', 76.00, 476, 'UNIMED']]

# total_price = 0.0


# for list_ in range(1, len(data)):
#     for index, item in enumerate(data[list_]):
#         if index == 2:
#             total_price = total_price + item

# print(total_price)




# lenght_side = int(input('Enter lenght side: '))
# i = 1

# for i in range(0, lenght_side+1):
#     if i:
#         print(lenght_side * '# ')
#         i =+ i



# size = 10
# sym = ['#',' ']
# desk = []

# for r,row in enumerate(range(size)):
#     line = []
#     for c,cell in enumerate(range(size)):
#         line.append(sym[(r+c)%len(sym)])
#     desk.append(''.join(line))
    
# print('\n'.join(desk))