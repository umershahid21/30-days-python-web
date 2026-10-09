
import time
import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# ==================================================
# PART A — TIMER DECORATOR
# ==================================================

# 1. Write timer(func) using time.perf_counter().
# 2. Apply it to slow_sum(n), which sums numbers 1..n.
# 3. Call slow_sum(1000000) and confirm timer output.
# 4. Why perf_counter() instead of time.time()?


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print(f"Execution time: {end_time - start_time:.6f} seconds")

        return result

    return wrapper


@timer
def slow_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


print("PART A — Timer")
print("Sum:", slow_sum(1000000))

# Answer:
# perf_counter() provides a high-resolution timer
# for measuring elapsed time accurately.


# ==================================================
# PART B — LOGGING DECORATOR
# ==================================================

# 1. Write log_call(func) using logging.info.
# 2. Configure logging.basicConfig(level=logging.INFO).
# 3. Apply it to multiply(a, b).
# 4. Call multiply(6, 7) and see two log lines.
# 5. Difference between logging.info and print?


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        logging.info(f"Before calling {func.__name__}")

        result = func(*args, **kwargs)

        logging.info(f"After calling {func.__name__}")

        return result

    return wrapper


@log_call
def multiply(a, b):
    return a * b


print("\nPART B — Logging")
print("Result:", multiply(6, 7))

# Answer:
# logging.info records structured messages with log levels,
# while print simply displays text.


# ==================================================
# PART C — AUTH DECORATOR WITH ARGUMENTS
# ==================================================

# 1. Write require_role(role).
# 2. Return actual_decorator, then wrapper.
# 3. Check CURRENT_USER["role"] against role.
# 4. Raise PermissionError when roles don't match.
# 5. delete_user(42) should succeed.
# 6. nuke_database() should raise PermissionError.
# 7. Explain which layer receives each argument.


CURRENT_USER = {"role": "admin"}


def require_role(role):

    # Layer 1 receives the required role.

    def actual_decorator(func):

        # Layer 2 receives the original function.

        @wraps(func)
        def wrapper(*args, **kwargs):

            # Layer 3 receives the function arguments.

            if CURRENT_USER["role"] != role:
                raise PermissionError(
                    f"Access denied! Required role: {role}"
                )

            return func(*args, **kwargs)

        return wrapper

    return actual_decorator


@require_role("admin")
def delete_user(user_id):
    return f"Deleted {user_id}"


@require_role("superuser")
def nuke_database():
    return "Boom"


print("\nPART C — Authorization")

print(delete_user(42))

try:
    print(nuke_database())

except PermissionError as error:
    print("Error:", error)


# Answer:
# Layer 1: require_role receives "admin".
# Layer 2: actual_decorator receives delete_user.
# Layer 3: wrapper receives 42 through *args.


# ==================================================
# PART D — STACKING DECORATORS
# ==================================================

# 1. Create calculate(n), which sums squares.
# 2. Decorate it with @timer and @log_call.
# 3. Call calculate(50000).
# 4. Explain which decorator's "before" runs first.


@timer
@log_call
def calculate(n):
    total = 0

    for i in range(1, n + 1):
        total += i ** 2

    return total


print("\nPART D — Stacking")
print("Calculated result:", calculate(50000))


# Answer:
# timer runs first because it is the outer decorator.
# It starts measuring time, then log_call runs and
# prints its "Before" logging message.
# After the function finishes, log_call logs "After",
# and finally timer prints the execution time.
