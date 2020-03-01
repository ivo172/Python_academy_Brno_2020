#test

a = 1

if a == 0:
    print("a je 1")
    quit()
else: print("a není 1")

print("End")





"""
# In the Python window you already have Mercedes and Rolls-Royce prices listed (don't forget to covert
# string to integer!). In addition, you have to create a variable that will ask the user for the extra cost. 
# Then you will need to calculate:
# 
# The price for two Mercedes,
# The Mercedes and Rolls-Royce prices,
# The price of two Rolls-Royce with extra equipment (each),
# Price for Mercedes with optional equipment.
# Finally, the program should print down everything clearly. Go ahead!
# """
# # Prices
# mercedes_cost = 150
# rolls_royce_cost = int('400')
#
# extra_cost = 0.95
# # extra cost (discount) fo two or more cars
#
# extra_equipment = 1.25
# # extra equipment on request
#
# order_car = input("You prefer Mercedes (1) or Rolls-Royce (2)?  ")
# print(f"You order is {order_car}")
#
# order_car = int(order_car)
#
# if order_car > 1:
#     order_cost = rolls_royce_cost
# else:
#     order_cost = mercedes_cost
#
# count_car = int(input("How many cars? "))
#
# if count_car > 1:
#     order_cost = order_cost * count_car * extra_cost
# else:
#     order_cost = order_cost * count_car
#
# print(f"Price {count_car} cars is {order_cost}")
#
# equipment = input("Do you need better equipment? (1/0) ")
# equipment = int(equipment)
#
# if equipment == 1:
#     total_cost = order_cost * extra_equipment
# else:
#     total_cost = order_cost
#
#
# print(f"Total price of your cars is {total_cost}!")
