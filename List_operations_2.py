# Results from the previous task
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']

# Interval 2-5

interval2_5 = employees[2:6]
print(f"From index 2 to 5 there are: {interval2_5}")

# Each 3rd

each3rd = employees[::3]
print(f"Every third member is: {each3rd}")

# Save index

jacob_index = employees.index("Jacob")

# Jacob index

print(f"Jacob is on the index: {jacob_index}")

# Number of name Agnes

agnes_count = employees.count("Agnes")
print(f"Number of repetitions of the name Agnes: {agnes_count}")