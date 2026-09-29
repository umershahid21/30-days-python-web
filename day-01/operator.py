
# Asks for two numbers, casting both inline to float.
# Prints the result of +, -, *, /, //, %, ** for those two numbers, each on its own labelled line (use f-strings).
# Asks for the user's age (inline int cast).
# Prints True or False for: is the age >= 18 and <= 65.
# Prints True or False for: is the age not equal to 0.
# Rules:

# All casting inline with input().
# Use snake_case.
# No if statements yet — just print the boolean expressions directly.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Modulus: {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")

age = int(input("Enter your age: "))
print (age >= 18 and age <= 65)
print (age != 0)
print(age>=18)
print(type(num1))
print(type(num2))


# division error comes when i add the num2 as 0, so i will add a try and except block to handle the error. but not now 
