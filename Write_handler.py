import os.path
path = os.path.dirname(__file__)

with open(path + '/text.txt', 'w') as handler_2:
    handler_2.write('text 11, text 22, text 33')


