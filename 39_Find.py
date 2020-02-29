def my_find(sequence, object):
    for index, element in enumerate(sequence):
        if element == object:
            return (index)
        else:
            continue
    return ('-1')


print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}], ('apple')))
