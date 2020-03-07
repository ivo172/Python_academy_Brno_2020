import random

dataset= [['Name','Item','Amount','Unit_Price']]

customers = ['Bettison, Elnora',
             'Doro, Jeffrey',
             'Idalia, Craig',
             'Conyard, Phil',
             'Skupinski, Wilbert',
             'McShee, Glenn',
             'Pate, Ashley',
             'Woodison, Annie']
products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
            ('Claravis', 9.85), ('Nadolol', 12.35),
            ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
            ('Metolazone', 43.06), ('PAXIL', 14.78)]

def generate_dataset(num_rows):

    for i in range(num_rows):

        name = random.choice(customers)
        item, price= random.choice(products)
        amount = random.randint(1,100)
        total_price = amount * price

        row = [name,item, amount, price, total_price]
        dataset.append(row)

    return dataset

print(generate_dataset(5))