# Create a function change_coins that will simulate a ticket machine in 
# that it will return the least possible amount of coins.
# Our machine should work with coins of the following 
# denominations: 1, 2, 5, 10, 20, 50
# For example, if the amount to be returned by the machine is 124, 
# the returned coins should be: two 50, one 20, two 2


def change_coins(amount, coins = [50,20,10,5,2,1]):
    coin_counts = {}

    for coin in coins:
        if not amount:
            break
        count,amount = divmod(amount,coin)
        if count:
            coin_counts[coin]=count

    return coin_counts

print(change_coins(145))
