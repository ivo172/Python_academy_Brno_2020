import os.path

path = os.path.dirname(__file__)

with open(path + '/text.txt') as handler:
    print(handler.readline())
    print(handler.tell())
    print(handler.readline())
    print(handler.tell())
    print(handler.readline())
    print(handler.tell())
    # print(handler)

    # function for read row number
    def read_specific_line(file_path, line_number: int) -> None:
        handler = open(file_path)
        current_line = None
        current_line_number = 0
        while current_line_number < line_number:
            current_line = handler.readline()
            current_line_number += 1
        print(current_line)


read_specific_line(path + '/text.txt', 3)
