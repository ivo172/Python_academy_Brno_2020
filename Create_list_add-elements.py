# Create Candidate

beginning = ["Francis", "Ann", "Jacob", "Claire"]

# Print candidates at the beginning

print(f"Employess at the beginning {beginning}")

# Create employees

employees = ["Bruno", "Agnes"]


# Print employees at the beginning

print(f"Candidates are {employees}")

# Add new candidates

beginning = beginning + employees

# Print new candidates

print(f"New candidates are {beginning}")

# Insert name

new_name = input("Insert name pls.: ")
new_name = (new_name)

beginning.append(new_name)

# Print the employees list after entering a new name
print(f"All employees: {beginning}")