# Write day-02/exceptions.py:

# Part A — Safe integer input
# Ask the user for a number. Cast it to int. Wrap in try/except ValueError. If invalid, print "Invalid input." If valid, print the number doubled.

# Part B — Safe division

# Ask for two numbers. Cast both inline. Do a / b. Handle:
# ValueError if either isn't a number → "Numbers only."
# ZeroDivisionError if b is 0 → "Cannot divide by zero."
# If no error, print the result with an f-string.

# Part C — Accessing a missing key
# Create a dict {"name": "Umer", "age": 24}. Try to access d["city"]. Handle KeyError and print "Key not found."

# Part D — File open with error handling
# Try to open "day-02/does_not_exist.txt" for reading inside a try/except FileNotFoundError block. Handle and print "File missing — skipping."

# Part E — finally (optional but do it)
# Wrap any of the above in a try/except/finally and print "Done." in the finally block. Run it with both good and bad input to see finally always print.

# Rules:
# Inline casts.
# snake_case.
# Specific exception types — do not use bare Exception except where I said it's okay.
# Keep the try block as small as possible — only put the risky line(s) inside. Don't wrap your whole file.

try:
    number = int(input("Enter a number: "))
    print(f"Number doubled: {number * 2}")
except ValueError:
    print("Invalid input.")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print(f"Result of division: {result}")
except ValueError:
    print("Numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")



d = {"name": "Umer", "age": 24}
try:
    city = d["city"]
except KeyError:
    print("Key not found.")

try:
    with open("day-02/does_not_exist.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File missing — skipping.")
finally:
    print("Done.")


