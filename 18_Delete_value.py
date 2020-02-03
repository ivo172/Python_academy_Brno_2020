
 # Your task is to complete the following instructions:
 #
 # - First of all we want to get the key which has alphabetically
 #   the maximal value - maximal_value_of_key,
 #
 # - second step is print that value out,
 #
 # - if maximal value in our dictionary is greater than the value of
 #   our maximal key (maximal_value_of_key), we want to delete the whole item
 #   under key maximal_value_of_key.
 #
 # - finally we want to print our new modified dictionary.

my_new_dict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 13579}

max_value_of_key = max(my_new_dict.keys())
# Find maximal key

print(f'Maximal value of key is "{max_value_of_key}".')
# Print maximal key

max_value = max(my_new_dict.values())
# Find maximal values and print
print(f'Maximal value is {max_value}')

value_max_value_of_key = my_new_dict.get(max_value_of_key)
# Show value from maximal key and print her.
print(f'Value from "{max_value_of_key}" is {value_max_value_of_key}')

if max_value > value_max_value_of_key:
    my_new_dict.pop(max_value_of_key)

print(my_new_dict)








