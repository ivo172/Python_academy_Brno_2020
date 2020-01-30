# ask the user for a number
# split the given number in halves (e.g. 123456 -> split to 123 and 456, 12345 -> 12 and 345)
# convert both halves into an integer
# if both halves are an even integer, print: 'Success' - e.g. 12 and 34
# if only the first part is even, print: 'First' - e.g. 12 and 345
# if the second part is even, print: 'Second' - e.g. 123 and 456
# if neither of the numbers is even print: 'Neither' - 123 and 455
# if nothing has been entered (the user just hit Enter), print: 'No input provided'


    
input_number = input("Please, give me a number: ")

if len(input_number) == 0:
    print("Not input provided")
else:    
    half_number = int(len(input_number)) // 2   #integer division
    first_half = int(input_number[:half_number])
    second_half = int(input_number[half_number:])

if len(input_number) == 0:
   pass
elif first_half % 2 == 0 and second_half % 2 == 0:
    print("Succsee")
elif first_half % 2 == 0 and second_half % 2 != 0:
    print("First")
elif first_half % 2 != 0 and second_half % 2 == 0:
    print("Second")
else:
    print("Neither")

