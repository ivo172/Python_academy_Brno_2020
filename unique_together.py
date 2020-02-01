str1 = 'New York'
str2 = 'Yorkshire'

unique_str = set(str1) ^ set(str2)
print(list(unique_str))
