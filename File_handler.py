import os.path
path = os.path.dirname(__file__)

handler_2 = open(path + '/text.txt')

# print(handler_2.read())

print(handler_2.readline())

print(handler_2.tell())

print(handler_2)

# function for read row number 

def read_specific_line(file_path, line_number: int) -> None:    
    handler_2 = open(file_path)
    current_line = None
    current_line_number = 0
    while current_line_number < line_number:
        current_line = handler_2.readline()
        current_line_number += 1
    print(current_line)

read_specific_line(path + '/text.txt', 3)


