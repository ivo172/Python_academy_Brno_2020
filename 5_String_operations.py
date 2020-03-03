# Save name

name = input("Name: ")

# Print name

print(f"Your name is: {name}")

# Save surname

surname = input("Surname: ")

# Print surname

print(f"Your surname is: {surname}")

# Create and print variable full_name

print(f"Your full name is {name} {surname}.")


# Create and print variable name_length

fullname = name + " " + surname
name_length = len(fullname)
print(f"Your full name has {name_length - 1} letters.")

# Print bounded variable full_name

print("=" * name_length)
print(fullname)
print("=" * name_length)
