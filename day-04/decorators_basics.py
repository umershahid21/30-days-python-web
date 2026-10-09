"""
Part A — Write the long way
Define def greet(name): return f"Hi, {name}".
Define def add_greeting(func) that returns a wrapper(*args, **kwargs) which prints "Before call", calls func(*args, **kwargs), prints "After call", and returns the result.
Assign wrapped_greet = add_greeting(greet).
Call wrapped_greet("Umer") and print the result.
Comment: what does add_greeting return? (one line)

Part B — Write the decorator way

Rewrite using @add_greeting on top of def greet(name): ....
Add from functools import wraps at the top and use @wraps(func) inside wrapper.
Call greet("Umer") and print the result.
Comment: @add_greeting above def greet is shorthand for what line of code? (one line)

Part C — Preserve metadata

Add a docstring to greet, e.g. Return a greeting for name..
Before adding @wraps(func): comment it out, run, print greet.__name__ and greet.__doc__. Paste what you see.
Uncomment @wraps(func), run again, print greet.__name__ and greet.__doc__. Paste what you see.
Comment: what did @wraps(func) preserve that was lost without it? (one line)

Part D — Reuse on another function
Define a different function def add(a, b): return a + b.
Decorate it with @add_greeting.
Call add(3, 4) — confirm the "Before call" / "After call" lines show up. Comment: the decorator worked on a function with a different signature than greet. Why? (one line — think about *args, **kwargs).

Rules:

functools.wraps — always use it.
snake_case.
Comment answers short and in your own words.
No decorators that take arguments yet — next file.
"""

def add_greeting(func):
    # Return a wrapper that prints before and after calling func.
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result

    return wrapper


@add_greeting
# Decorate the greet function with add_greeting.
def greet(name):
    # Return a greeting for name.
    return f"Hi, {name}"

wrapped_greet = add_greeting(greet)

print(wrapped_greet("Umer"))


    