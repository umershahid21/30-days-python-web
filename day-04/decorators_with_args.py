
"""
YOUR ASSIGNMENT — DAY 04: DECORATORS WITH ARGUMENTS

Part A — Write a repeat decorator

Write def repeat(times) with the three-layer structure.
The wrapper should call the function times times in a loop.
The wrapper should return the last result.
Use @wraps(func) on the innermost wrapper.

Part B — Test it

Decorate a function:

@repeat(3)
def say_hi(name):
    print(f"Hi {name}")

Call say_hi("Umer").
You should see "Hi Umer" printed three times.

Now decorate def add(a, b): return a + b with
@repeat(2), call add(3, 4), and print the result.

Comment:
Why does the result show up only once at the end,
even though the function ran twice?

Comment:
How many times was repeat called?
How many times was actual_decorator called?
How many times was wrapper called?
(Answer three numbers.)

Part C — A more useful example: log_prefix

Write a decorator log_prefix(prefix) that takes a string.
The wrapper should print:

f"{prefix}: calling {func.__name__}"

before calling the function.

Test:

@log_prefix("[INFO]")
def greet(name):
    return f"Hi, {name}"

@log_prefix("[DEBUG]")
def farewell(name):
    return f"Bye, {name}"

Call both and print their results.

Comment:
What does log_prefix("[INFO]") return?
What does the returned thing then do?

Part D — Decorator with a default argument

Modify repeat to accept a default value:
def repeat(times=2)

Test @repeat() and @repeat(4).

Comment:
When you write @repeat() with empty parentheses,
what's happening?

Rules:
- from functools import wraps at the top.
- @wraps(func) on the innermost wrapper.
- Three layers — indentation matters.
- Comments in your own words.
- snake_case.
"""

from functools import wraps


# ==========================================
# PART A — REPEAT DECORATOR
# ==========================================

def repeat(times=2):

    # Layer 1: Receives the number of repetitions.

    def actual_decorator(func):

        # Layer 2: Receives the original function.

        @wraps(func)
        def wrapper(*args, **kwargs):

            # Layer 3: Receives arguments and runs the function.
            result = None

            for i in range(times):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return actual_decorator


# ==========================================
# PART B — TEST THE DECORATOR
# ==========================================

@repeat(3)
def say_hi(name):
    print(f"Hi {name}")


print("PART B — say_hi")
say_hi("Umer")


@repeat(2)
def add(a, b):
    return a + b


print("\nPART B — add")
print(add(3, 4))


# Answer 1:
# The function runs twice, but we only print
# the last returned result once.

# Answer 2:
# For the two decorated functions above:
# repeat was called 2 times.
# actual_decorator was called 2 times.
# wrapper was called 2 times.
#
# Note: The original functions executed
# 3 + 2 = 5 times in total.


# ==========================================
# PART C — LOG PREFIX DECORATOR
# ==========================================

def log_prefix(prefix):

    # Layer 1: Receives the prefix.

    def actual_decorator(func):

        # Layer 2: Receives the original function.

        @wraps(func)
        def wrapper(*args, **kwargs):

            # Layer 3: Prints the prefix and calls the function.
            print(f"{prefix}: calling {func.__name__}")

            result = func(*args, **kwargs)

            return result

        return wrapper

    return actual_decorator


@log_prefix("[INFO]")
def greet(name):
    return f"Hi, {name}"


@log_prefix("[DEBUG]")
def farewell(name):
    return f"Bye, {name}"


print("\nPART C — log_prefix")
print(greet("Umer"))
print(farewell("Umer"))


# Answer 1:
# log_prefix("[INFO]") returns actual_decorator.

# Answer 2:
# actual_decorator receives the function
# and returns its wrapper.


# ==========================================
# PART D — DEFAULT ARGUMENT
# ==========================================

# We already defined repeat(times=2) in Part A.


@repeat()
def hello(name):
    print(f"Hello {name}")


@repeat(4)
def goodbye(name):
    print(f"Goodbye {name}")


print("\nPART D — Default repeat")
hello("Umer")

print("\nPART D — Explicit repeat")
goodbye("Umer")


# Answer:
# @repeat() calls repeat without passing a number,
# so Python uses the default value of 2.
