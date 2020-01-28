# Your task is to create a script called birth_year.py that will:
# - ask the user for his/her age
# - calculate the year the person was born in
# - print the resulting year

import datetime

your_age = input("How old you? ")

today_year = datetime.date.today().year

print(f"You were (probably) born in {int(today_year) - int(your_age)}")
