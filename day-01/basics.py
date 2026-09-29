# Asks the user for their name (a string).

# Asks for their age (cast to int).

# Asks for their height in meters (cast to float).

# Prints a single line using an f-string that shows all three, e.g.:
# Umer is 24 years old and 1.75m tall.

# Also prints the type of each of the three variables on separate lines, using type().

name= input("What is your name? ")
age_s= input("What is your age? ")
age= int(age_s)
height= input("What is your height in meters? ")
height= float(height)

print(f"{name} is {age} years old and {height}m tall")
print(type(name))
print(type(age))
print(type(height))