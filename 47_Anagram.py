# The goal in this assignment is to create a function all_anagrams that takes
# a list of 2 or more strings as input and returns boolean value telling us,
# whether all the strings inside the list are anagrams or not.

def all_anagrams(words):
    if words:
        result = True
        seq = sorted(words.pop())
        for word in words:
            if seq != sorted(word):
               result = False
    else:
        result = False
    return result


print(all_anagrams(['ship', 'hips']))