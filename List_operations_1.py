# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']

print(f"Employees: {employees}")
print(f"New candidates: {candidates}")

# Delete names from candidates

deleted_candidate = candidates.pop(0)

print(f"Was deleted: {deleted_candidate}")

# Print remaining candidates

print(f"Employees at the beginning: {candidates}")

# Repeat element

repetition_candidate = candidates * 3

# Print repeating element in list candidates

print(f"Repetition of Agnes in the candidate list: {repetition_candidate}")

# Join lists

employees = employees + repetition_candidate

# Print joined lists

print(f"Joined candidates and employees: {employees}")

# Index 2

index2 = employees[2]

print(f"On index 2 is: {index2}")

# Find out last index and assign it to variable

last_index = employees[-1]
max_index = len(employees)

# Last index

print(f"On index {max_index} is: {last_index}")

