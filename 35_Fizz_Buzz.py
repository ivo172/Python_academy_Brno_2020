for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print(f'Fizz Buzz')
        else:
            print(f'Fizz')
    elif number % 5 == 0:
        print(f'Buzz')

    else:
        print(number)

