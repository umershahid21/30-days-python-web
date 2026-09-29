# Part A — Grade as a function
# Rewrite Part A from control_flow.py as a function:
# def get_grade(marks):
#     # return "A" / "B" / "C" / "D" / "F"
# Then call it with a few test values (95, 82, 71, 65, 40) and print the results.

# Part B — Return vs print
# Write two functions:
# square_print(n) — prints n*n
# square_return(n) — returns n*n
# Then:
# Assign square_print(4) to a variable and print that variable.
# Assign square_return(4) to a variable and print that variable.
# Observe the difference — write a one-line comment above each explaining what you got.

# Part C — Default argument
# def introduce(name, role="student"):
# Returns a sentence like "Umer is a student." or "Sara is a developer."
# Call it once without role, once with role.

# Rules:
# Functions must return, not print (except square_print, obviously).
# snake_case, f-strings.
# Test calls at the bottom of the file, not inside the functions.


def get_grade(marks):
    if marks >=90:
        return "A"
    elif marks >=80:
        return "B"
    elif marks >=70:
        return "C"
    elif marks >=60:
        return "D"
    else:
        return "F"

grade1 = get_grade(95)
grade2 = get_grade(82)
grade3 = get_grade(71)
grade4 = get_grade(65)
grade5 = get_grade(40)

print(f"grade1 is {grade1}")
print(f"grade2 is {grade2}")
print(f"grade3 is {grade3}")
print(f"grade4 is {grade4}")
print(f"grade5 is {grade5}")

def square_print(n):
    print(n*n)

def square_return(n):
    return n*n

square_print_value = square_print(4)
print(f"square_print_value is {square_print_value}")


square_return_value = square_return(4)
print(f"square_return_value is {square_return_value}")

def introduce(name, role="student"):
    return f"{name} is a {role}."

print(introduce("Umer"))
print(introduce("Sara", "developer"))