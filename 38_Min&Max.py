def my_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number <= min_number:
            min_number = number
        else:
            continue
    return min_number


def my_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number >= max_number:
            max_number = number
        else:
            continue
    return max_number

print(my_min([8, 16, 56, 41, 2, 55]))
print(my_max([8, 16, 56, 41, 2, 55]))
