import os.path
path = os.path.dirname(__file__)

with open(path + '/text.txt', 'w') as handler_2:
    handler_2.write('text1\ntext2')


