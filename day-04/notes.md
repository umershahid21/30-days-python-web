# Day 4 — Advanced Functions & Decorators

Repo: `30-days-python-web` · Branch: `main`

---

## 1. Functions as First-Class Objects

In Python, functions are **values**, just like numbers or strings. That means three things:

1. You can **assign** a function to a variable.
2. You can **pass** a function as an argument to another function.
3. You can **return** a function from another function.

### Assigning a function

```python
def greet(name):
    return f"Hi, {name}"

say_hi = greet          # NO parentheses — this is the function object
print(say_hi("Umer"))   # "Hi, Umer"
```

**The rule:**
- `greet` → the function object itself
- `greet()` → calls the function (must provide required arguments)

`say_hi = greet()` **calls** `greet` first and assigns its **return value**. It's usually a bug — you probably wanted `say_hi = greet` (the function itself).

### Passing functions as arguments

```python
def add(a, b): return a + b
def subtract(a, b): return a - b

def calculate(operation, x, y):
    return operation(x, y)

print(calculate(add, 10, 4))       # 14
print(calculate(subtract, 10, 4))  # 6
```

`operation` is a parameter that holds a **function**. You pass `add` (no parentheses), and `calculate` calls it internally.

You already use this pattern with `sorted(..., key=...)`, `map()`, `filter()`, `min(..., key=...)`.

### Returning functions (closures)

```python
def make_greeter(greeting):
    def inner(name):
        return f"{greeting}, {name}"
    return inner

hello = make_greeter("Hello")
salam = make_greeter("Salam")

print(hello("Umer"))    # "Hello, Umer"
print(salam("Umer"))    # "Salam, Umer"
```

**Closure:** the inner function captures the outer function's variables. `greeting` stays alive even after `make_greeter` returns, because `inner` still refers to it.

---

## 2. Decorators — The Core Idea

A **decorator** is a function that **takes a function**, wraps it with extra behavior, and returns the wrapped version.

### The long way (no syntax sugar)

```python
def add_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done")
        return result
    return wrapper

def say_hello(name):
    return f"Hello, {name}"

say_hello = add_logging(say_hello)   # ← replace with wrapped version
say_hello("Umer")
```

The original `say_hello` was never modified. It got **wrapped**.

### The decorator syntax (`@`)

```python
@add_logging
def say_hello(name):
    return f"Hello, {name}"
```

**The `@` is literal shorthand for:**
```python
say_hello = add_logging(say_hello)
```

That's the entire magic. Everything else is convention.

### `*args` and `**kwargs`

The wrapper must accept whatever arguments the wrapped function accepts:

```python
def wrapper(*args, **kwargs):
    ...
    result = func(*args, **kwargs)   # unpack them back
    return result
```

- `*args` → tuple of positional arguments
- `**kwargs` → dict of keyword arguments

Without these, the decorator only works on functions with a specific signature. With them, it works on **any** function.

### The boilerplate template (memorize this)

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```

---

## 3. `functools.wraps` — Preserving Metadata

### The problem

When you decorate:
```python
@add_logging
def greet(name):
    """Return a greeting."""
    return f"Hi, {name}"
```

Python does `greet = add_logging(greet)`. Now `greet` points to `wrapper`, not the original function.

```python
print(greet.__name__)   # "wrapper"   ← wrong!
print(greet.__doc__)    # None        ← lost!
```

**Original metadata is gone** — name, docstring, module, type annotations. All overwritten by `wrapper`'s (empty) versions.

### Why it matters

- **Tracebacks** become useless: `in wrapper at line 12` — you don't know which function actually failed.
- **Frameworks break:** FastAPI reads `__name__` and `__doc__` to generate API docs and routes. Every decorated route shows up as `wrapper` in the docs.
- **Debugging tools** (profilers, `help()`, IDEs) can't identify the function.

### The fix

```python
from functools import wraps

def add_logging(func):
    @wraps(func)               # ← one line, copies metadata from func to wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**What `@wraps(func)` does:** copies `__name__`, `__doc__`, `__module__`, `__annotations__`, `__qualname__` from `func` onto `wrapper`, and sets `wrapper.__wrapped__ = func`.

**Rule:** every decorator you write gets `@wraps(func)` on the inner wrapper. No exceptions.

---

## 4. Decorators That Take Arguments

Plain decorators have **2 layers**. Decorators with arguments have **3 layers** — one extra to receive the decorator's configuration.

### The problem

```python
@repeat(3)              # ← decorator with an argument
def say_hi(): ...
```

You're calling `repeat(3)` first — that returns *something*, and that *something* then decorates `say_hi`.

### The three-layer structure

```python
from functools import wraps

def repeat(times):                          # layer 1 — receives 3
    def actual_decorator(func):             # layer 2 — receives say_hi
        @wraps(func)
        def wrapper(*args, **kwargs):       # layer 3 — receives say_hi's arguments
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper                      # layer 2 returns wrapper
    return actual_decorator                 # layer 1 returns actual_decorator
```

**Indentation matters:**

```python
def repeat(times):               # 0 spaces
    def actual_decorator(func):  # 4 spaces
        @wraps(func)             # 8 spaces
        def wrapper(...):        # 8 spaces
            ...                  # 12 spaces
        return wrapper           # 8 spaces
    return actual_decorator      # 4 spaces
```

**Trace it for `@repeat(3)`:**
1. `repeat(3)` → returns `actual_decorator`
2. `actual_decorator(say_hi)` → returns `wrapper`
3. `say_hi` is now `wrapper`

### Common beginner mistake

Putting `@wraps(func)` on `actual_decorator` instead of `wrapper`. **`@wraps` always goes on the innermost function** — the one that actually replaces the original.

### Default arguments

```python
def repeat(times=2):
    ...
```

Now `@repeat()` uses `times = 2`, and `@repeat(4)` uses 4. Both work because `@repeat()` just calls `repeat()` with no arguments → default value.

### When to use argument-taking decorators

- `@retry(times=3)` — behavior depends on a setting
- `@log_prefix("[INFO]")` — control the prefix
- `@require_role("admin")` — check for a specific permission
- `@app.route("/users")` — FastAPI, Flask route definition

If the decorator's behavior depends on a **parameter**, it needs 3 layers.

---

## 5. Practical Decorator Patterns

### Timer decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper
```

**`time.perf_counter()` — not `time.time()`:**
- `perf_counter` is **monotonic** — it only moves forward. System clock changes (NTP sync, DST, user changes the clock) don't affect it.
- It has **higher resolution** (nanoseconds) than `time.time()`.
- `time.time()` is for wall-clock time; `perf_counter` is for **measuring durations**.

### Logging decorator

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"CALL {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"RETURN {func.__name__} -> {result!r}")
        return result
    return wrapper
```

**`logging` vs `print`:**
- `logging` has **levels** (DEBUG, INFO, WARNING, ERROR, CRITICAL) — you can filter what shows.
- `logging` can go to **files, sockets, log aggregators** (Sentry, Datadog) — not just stdout.
- `logging` is **configurable** without editing code (`basicConfig(level=...)`).
- `print` is hardcoded, always fires, no structure.
- **Production code uses `logging` everywhere.**

**`!r` in f-strings:** formats with `repr()` instead of `str()`. Strings get quotes. Critical for logs — `"Hello"` is clearer than `Hello` when you need to know the type.

### Auth/permission decorator (with argument)

```python
from functools import wraps

CURRENT_USER = {"role": "admin"}

def require_role(role):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_USER["role"] != role:
                raise PermissionError(f"Requires role: {role}")
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@require_role("admin")
def delete_user(user_id):
    return f"Deleted {user_id}"
```

**Key pattern:** the wrapper **checks before calling**. If the check fails, the function **never runs**. This is a real security pattern — FastAPI, Django, Flask all use it.

### Stacking decorators

```python
@timer
@log_call
def process():
    ...
```

Equivalent to `process = timer(log_call(process))`.

**Order matters:**
- The **bottom** decorator wraps first (closest to the function).
- The **top** decorator wraps last (becomes the outermost layer).
- **Execution order:** top's "before" → bottom's "before" → function → bottom's "after" → top's "after".

**Practical implication:** swapping the order changes behavior. If `@timer` is on top, the log lines are *inside* the timing window. If `@log_call` is on top, the timing is *inside* the log window.

---

## 6. Key Gotchas (Day 4)

1. **`func` vs `func()`** — without parentheses: the function object. With: the result of calling it.
2. **`*args, **kwargs`** in wrappers — needed to handle any function signature.
3. **`@wraps(func)` is not optional.** Missing it breaks tracebacks, frameworks, and tooling.
4. **`@wraps` goes on the innermost `wrapper`**, not on `actual_decorator`.
5. **Three layers for argument-taking decorators** — the extra layer receives the decorator's argument.
6. **Wrapper can block execution.** If a decorator raises before calling `func`, the function never runs.
7. **Stacking order matters.** Top decorator is outermost. Swap and behavior changes.
8. **`perf_counter` for timing, not `time.time()`.** Monotonic and higher resolution.
9. **`logging` for production, `print` for scripts.** Never `print` in library code.

---

## 7. Day 4 Files Created

```
day-04/
├── first_class_functions.py      # assign/pass/return functions, closures, sorted(key=...)
├── decorators_basics.py          # @syntax, functools.wraps, metadata
├── decorators_with_args.py       # three-layer decorators, repeat, log_prefix
├── practical_decorators.py       # timer, logging, auth, stacking
└── notes.md                      # this file
```