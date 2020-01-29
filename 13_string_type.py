# Ask user for any string
# Determine, whether the string entered
# contains only numbers - digits - in that case the program should print to the terminal: 'Numeric'
# contains only letters - in that case the program should print to the terminal: 'Letters Only'
# otherwise print to terminal: 'Mixed'

string = input("Give me some input: ")

if string.isalpha():
    print("Letters only")
elif string.isdigit():
    print("Numeric")
else:
    print("Mixed")                