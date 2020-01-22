"""
Create a program, that will use the indexing to print and extract:
first 5 letters in word 'indexing',
last 5 letters in word 'indexing',
first letter in word 'indexing', then stepping by 3.
Example of running program:
First five letters: index
Last five letters: exing
Every third letter: ien
Save each slice in a variable and then print variable in sentence (for example 'First five letters: ' + variable).
"""

word_indexing = "indexing"      # string

# Extract and print first 5 letters
first_five = (word_indexing[0:5])

# Extract and print last 5 letters
last_five = (word_indexing[-5:-1])

# Extract and print each 3rd letter
every_third = (word_indexing[::3])

print(f"First five letters are ´{first_five}´, last five letters are ´{last_five}´ and every third letter is ´{every_third}´.")