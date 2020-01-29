# Your task is to create a script called convert_day.py that will: ask for a number between 1 to 7 return the name of
# corresponding weekday (1 - 'Monday', 2-'Tuesday', 3 - 'Wednesday', 4 - 'Thursday', 5 - 'Friday', 6 - 'Saturday',
# 7 - 'Sunday') if no input has been provided (user hitting enter without typing anything), the program should print:
# 'No input provided' if the input is not a number the program should print: 'Enter only numbers, please'

weekday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

selected_number = input("Please enter number of the day: ")

if selected_number.isalpha():
    print("Enter only number, please.")
elif int(selected_number) < 1 or int(selected_number) > 7:
        print("Number in range 1 to 7, please!")
else:
    selected_day = weekday[int(selected_number) - 1]
    print(selected_day)



