
import datetime     # import library datetime

# Greet the client
print("=" * 80)
print("Welcome in Destination \na place to choose a holiday!!!")
print("=" * 80)

# Offer destinations
print("Offer of holiday destinations:")
print("=" * 80)
print("1 - Prague  | 1000\n2 - Wien    | 1100\n3 - Brno    | 2000\n4 - Svitavy | 1500\n5 - Zlin    | 2300\n6 - Ostrava "
      "| 3400")
print("=" * 80)

# Get input from user about destination

user_choise = input("Select destination: ")

# Assign variables appropriate data

offers = {
    1: {"city": "Prague", "cost": 1000},
    2: {"city": "Wien", "cost": 1100},
    3: {"city": "Brno", "cost": 2000},
    4: {"city": "Svitavy", "cost": 1500},
    5: {"city": "Zlín", "cost": 2300},
    6: {"city": "Ostrava", "cost": 3400}
}

# Get data from variables based on user's input

user_choise = int(user_choise)
city = offers[user_choise]["city"]
cost = offers[user_choise]["cost"]

# For destinations Svitavy and Ostrava we offer a special discount of 25%. We cannot provide our services to clients:

if city == "Svitavy":
    cost = cost * 0.75
    print(f"Good choice, we have a 25% discount for this destination")
elif city == "Ostrava":
    cost = cost * 0.75
    print(f"Good choice, we have a 25% discount for this destination")
else:
    cost = cost

# Introduce registration
print("_" * 80)
print("Please register to complete your order:")
print("_" * 80)

# Get input from user about personal data

first_name = input("Name: ")
second_name = input("Second name: ")
year_birth = input("Year of birth: ")

year = datetime.date.today().year   # extract actual year

age = year - int(year_birth)

if age <= 14:
    print("Only for ages 15 and older, game over!")
    exit()

email = input("email: ")

is_et_email = email.find("@")   # when it finds @, returns -1

if is_et_email == -1:
    print("Bad email address!")
    exit()

password: str = input("Password: ")

num_password = len(password)

if num_password < 8:    # password min. 8 characters
    print("Min. 8 characters pls.")
    exit()

first_password = password[0]
last_password = password[-1]

first_password_ok = first_password.isnumeric()  # first character cannot be a number!
last_password_ok = last_password.isnumeric()    # last character cannot be a number!
a1z_password_ok = password.isalnum()    # password must contain number(s) and letter(s)!

if first_password_ok:   # if True - exit
    print("Password error")
    exit()

if last_password_ok:    # if True - exit
    print("Password error")
    exit()

if not a1z_password_ok:     # if not True - exit
    print("Password error")
    exit()

print("=" * 80)

# Thank user by the input name and inform him/her about the reservation made

print(f"Thank you for registering, Mr / Mrs {first_name} {second_name}")
print(f"Your reservation {city} and price {cost}")
