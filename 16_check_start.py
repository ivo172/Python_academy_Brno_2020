# Your task is to create a script called check_start.py that will:
# - ask the user for the secret password
# - if the password given, starts with any of the lowercase 'a','e','f','q','z', print to the terminal 'Welcome!'
# - otherwise print 'The input does not match'

enter_pass = input("Enter the secret password: ")

first = enter_pass[0]

if first in ("a", "e", "f", "q","z"):
    print("Welcome")
else: 
    print("The input does not match")

        