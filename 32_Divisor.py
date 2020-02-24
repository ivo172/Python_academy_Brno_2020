# Write a program that will work with three inputs:
# - integer start
# - integer stop
# - integer divisor
# All of them should be provided by the user.

# The program should:
# - generate a collection of integers in range between start (including) and stop (included in the collection)
# - print a list of only those numbers in range start - stop, that are divisible by divisor
# If divisor is 0, the program should print to the terminal a string 'Cannot divide by zero' instead of the list of divisible numbers

start = int(input('START: '))
stop = int(input('STOP: '))
divisor = int(input('DIVISOR: '))
number = int()
numbers = []

if divisor == 0:
    print('Cannot divide by zero')
    quit()
    
for number in range(start, stop + 1):
    if number % divisor == 0:
        numbers.append(number)

print(numbers)
    
