"""
Your question (Part A — first-class functions)
Write day-04/first_class_functions.py:
1. Assign a function to a variable
Define def greet(name): return f"Hi, {name}".
Assign greet to say_hi (no parentheses).
Call say_hi("Umer") and print the result.
Comment: what would happen if you wrote say_hi = greet() instead? Explain in one line.

2. Pass a function as an argument
Define def add(a, b): return a + b.
Define def subtract(a, b): return a - b.
Define def calculate(operation, x, y): return operation(x, y).
Call calculate(add, 10, 4) and calculate(subtract, 10, 4) — print both.
Comment: in calculate, operation is a parameter. What is it holding? (one sentence)

3. Return a function (closure)
Define make_greeter(greeting) that returns an inner function taking name and returning f"{greeting}, {name}".
Create hello_greeter = make_greeter("Hello") and salam_greeter = make_greeter("Salam").
Call each with a name and print both results.
Comment: when hello_greeter("Umer") runs, where does "Hello" come from? (one sentence)

4. Real-world use of passing functions
Create words = ["banana", "apple", "cherry"].
Print sorted(words) — alphabetical.
Print sorted(words, key=len) — sorted by length. Comment: what does key=len actually pass to sorted?
Print sorted(words, key=lambda w: w[-1]) — sorted by last letter. (You'll learn lambda properly later; for now just observe.)

Rules:
snake_case.
Comment answers should be short and in your own words.
Don't touch decorators yet — this file is about the underlying concept.
"""

def greet(name):
    return f"Hi, {name}"

say_hi=greet
print(say_hi("Umer"))
# If you wrote say_hi = greet(), it would call greet immediately and assign its return value to say_hi, instead of the function itself.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, x, y):
    return operation(x, y)

print(calculate(add, 10, 4))
print(calculate(subtract, 10, 4))
# In calculate, operation is holding a reference to a function that can be called with x and y.


def make_greeter(greeting):
    def inner(name):
        return f"{greeting}, {name}"
    return inner

hello_greeter = make_greeter("Hello")
salam_greeter = make_greeter("Salam")

print(hello_greeter("Umer"))
print(salam_greeter("Umer"))
# When hello_greeter("Umer") runs, "Hello" comes from the closure created by make_greeter.

words = ["banana", "apple", "cherry"]
print(sorted(words))  # Alphabetical
print(sorted(words, key=len))  # Sorted by length
# key=len passes the len function to sorted, which is used to determine the sorting order based on the length of each word.
print(sorted(words, key=lambda w: w[-1]))
