'''
<<<<<<< HEAD
Write a Python script that will ask the user to enter a number from which it will 
compute the result. The result should be the sum of numbers less than or equal 
to the input number, each raised to power of its value. 
Then the script should print the result to the terminal.

For example:
- if the user enters number 5, the program should compute the sum as: 1**1 + 2**2 + 3**3 + 4**4 + 5**5.
- if the user enters 6, then it should be: 1**1 + 2**2 + 3**3 + 4**4 + 5**5 + 6**6
...and so on. '''
=======
Write a Python script that will ask the user to enter a number 
from which it will compute the result. 
The result should be the sum of numbers less than or equal to 
the input number, each raised to power of its value. 
Then the script should print the result to the terminal.
For example:
- if the user enters number 5, the program should compute the sum as: 
  1**1 + 2**2 + 3**3 + 4**4 + 5**5.
- if the user enters 6, then it should be: 1**1 + 2**2 + 3**3 + 
  4**4 + 5**5 + 6**6
...and so on.
'''
i = 1
result = 0

number = int(input('Please enter your number: '))
 
while number >= i:
    num = i ** i
    result = result + num
    i = i + 1

print(f'The result is:  {result}')
>>>>>>> 74ad46578467f88d968a5850bad1db1a77ce2d8a
