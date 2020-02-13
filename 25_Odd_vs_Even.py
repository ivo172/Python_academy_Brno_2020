# Write a Python script that will sum all the even numbers and odd numbers separately. 
# At the end the program should print to terminal the absolute value of the difference 
# between the two sums of odd and even numbers.

nums = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]

even = []
odd = []
even_nums = []
odd_nums = []

for num in nums:
    if num %2 == 0:
        even_nums.append(num)
        continue
    else:
        odd_nums.append(num)

print(f'Even numbers: {even_nums}')
print(f'Odd numbers: {odd_nums}')

sum_even = 0

for num in even_nums:
    sum_even = sum_even + num

sum_odd = 0

for num in odd_nums:
    sum_odd = sum_odd + num

print(f'The difference is {abs(sum_even - sum_odd)} ')