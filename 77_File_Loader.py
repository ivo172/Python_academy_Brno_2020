def file_loader(filepath):

    try:
        file = open(filepath)

    except FileNotFoundError:
        filename = filepath.split('/')[-1]
        print('File {} does not exist.'.format(filename))

    else:
        content = file.read()
        file.close()
        return content


filepath = input('Enter filepath: ')
print(file_loader(filepath))
