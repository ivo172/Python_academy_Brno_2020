# We would like to find out, what numbers in a given range are divisible by each of the numbers btw. 2 and 9.
# Your task is to create a program that will:
# - collect the information about numbers divisible by each single digit number between 2 and 9
# - print the information in nicely formatted table


start_point = int(input('Start point: '))
end_point = (int(input('End point: '))) + 1

i = 2


def string_x(start_point, end_point, i):  # i = divisor
    num_ = ''
    for num in range(start_point, end_point):
        if num % i == 0:
            num_ = num_ + ' ' + str(num)
    return num_


print('| Divisor |    Number Divided    |')       
print('==================================')

for i in range(2, 10):
    result = string_x(start_point, end_point, i)
    print(f'|{i:^9}|{result:^22}|')
