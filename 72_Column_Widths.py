# Create a function get_widths that will calculate column width (number of characters) for each column in a given
# table. It should return a list of the widths of the columns from left to right.

texts = [['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
['Conyard, Phil', 'WRINKLESS PLUS', 49, 23.55, 1153.95],
['Bettison, Elnora', 'Doxycycline Hyclate', 59, 23.43, 1382.37],
['Skupinski, Wilbert', 'Metolazone', 51, 43.06, 2196.06],
['McShee, Glenn', 'Claravis', 1, 9.85, 9.85]]

def get_widths(table):
    width = []
    lines = {}
    i = 0

    for word in table:
        for column in word:
            width.append(len(str(column)))
        else:
            width.append('_')

    while width:
        index = width.index('_')  # find position '_' in string
        i = i + 1
        x = (width[:index])
        line = {i : x}      # create key:value from first line in dictionary "line"
        lines.update(line)
        width[:index + 1] = []  # delete first row from "width"

    for key in lines:
        print(key)


    return lines


print(get_widths(texts))



