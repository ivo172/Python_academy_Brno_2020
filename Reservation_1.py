# Greet the client

print("="*80)
print("Welcome in Dovolenkovnik \na place to choose a holiday!!!")
print("="*80)

# Offer destinations
print("Offer of holiday destinations:")
print("="*80)
print("1 - Prague  | 1000\n2 - Wien    | 1100\n3 - Brno    | 2000\n4 - Svitavy | 1500\n5 - Zlin    | 2300\n6 - Ostrava "
      "| 3400")
print("="*80)

# Get input from user about destination

user_choise = input("Select destination: ")

# Assign variables appropriate data

offers = {
    1:{"city":"Prague", "cost":1000},
    2:{"city":"Wien", "cost":1100},
    3:{"city":"Brno", "cost":2000},
    4:{"city":"Svitavy", "cost":1500},
    5:{"city":"Zlín", "cost":2300},
    6:{"city":"Ostrava", "cost":3400}
}

# Get data from variables based on user's input

user_choise =int(user_choise)
city = offers[user_choise]["city"]
cost = offers[user_choise]["cost"]


# Introduce registration
print("_"*80)
print("Please register to complete your order:")
print("_"*80)

# Get input from user about personal data

first_name = input("Name: ")
second_name = input("Second name: ")
year_birth = input("Year of birth: ")
email = input("email: ")
heslo = input("Password: ")
print("="*80)

# Thank user by the input name and inform him/her about the reservation made

print(f"Thank you for registering, Mr / Mrs {first_name} {second_name}")
print(f"Your reservation {city} and price {cost}")
# End
