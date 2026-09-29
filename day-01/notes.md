# Day 1 — Python Fundamentals (Revision Notes)

Repo: `30-days-python-web` · Branch: `main`

---

## 1. Variables

A variable is a **name pointing to a value in memory**.

```python
name = "Umer"
age = 24
```

- Python is **dynamically typed** — no declarations, Python infers the type.
- Reassigning to a different type is allowed but bad practice.
- Use `snake_case` for variables and functions: `user_name`, `total_price`.
- Names must start with a letter or `_`, no spaces, no hyphens.
- Names should be meaningful: `user_age`, not `x`.

---

## 2. Data Types

| Type | Example | Notes |
|---|---|---|
| `int` | `42`, `-7` | whole numbers |
| `float` | `3.14`, `-0.5` | decimal numbers |
| `str` | `"hello"` | text |
| `bool` | `True`, `False` | capitalized |
| `NoneType` | `None` | "no value" |
| `list` | `[1, 2, 3]` | ordered, changeable |
| `tuple` | `(1, 2, 3)` | ordered, unchangeable |
| `dict` | `{"name": "Umer"}` | key → value pairs |
| `set` | `{1, 2, 3}` | unique, unordered |

Check type with `type()`:

```python
type(10)       # <class 'int'>
type(3.14)     # <class 'float'>
type("hello")  # <class 'str'>
type(True)     # <class 'bool'>
```

**Important:** `input()` **always** returns a `str`. Cast it before doing math.

---

## 3. Type Casting

### Explicit (you do it)
```python
int("24")        # 24
float("19.99")   # 19.99
str(100)         # "100"
bool(1)          # True
```

Inline with input:
```python
age = int(input("Age: "))
```

### Implicit (Python does it)
```python
10 + 2.5   # 12.5  (int → float automatically)
```

### Common crash
```python
int("hello")      # ❌ ValueError
int("3.5")        # ❌ ValueError (use float first)
int(float("3.5")) # ✅ 3
```

When you see `ValueError: invalid literal for int()`, the string wasn't a valid integer.

---

## 4. Operators

### Arithmetic
| Op | Meaning | Example |
|---|---|---|
| `+` | add | `10 + 3` → `13` |
| `-` | subtract | `10 - 3` → `7` |
| `*` | multiply | `10 * 3` → `30` |
| `/` | divide (always float) | `10 / 3` → `3.333…` |
| `//` | floor divide | `10 // 3` → `3` |
| `%` | modulus (remainder) | `10 % 3` → `1` |
| `**` | power | `10 ** 3` → `1000` |

Note: `/` always returns a **float** (`10 / 2` → `5.0`).
Note: `%` is **not percent** — it's remainder. `x % 2 == 0` checks even.

### Comparison (returns bool)
`==` `!=` `>` `<` `>=` `<=`

**Never** confuse `=` (assign) with `==` (compare). `if x = 5:` is a `SyntaxError`.

### Logical
`and` (both) · `or` (either) · `not` (flip)

### Can't mix types carelessly
```python
"5" + "3"   # "53"  (string concat)
5 + 3       # 8
"5" + 3     # ❌ TypeError
```

---

## 5. Control Flow

### if / elif / else
```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("F")
```

- Checked **top-down**; first `True` wins.
- `else` is optional.
- **Indentation is syntax.** 4 spaces.

### Truthy / Falsy
Falsy: `""`, `0`, `[]`, `{}`, `None`, `False`
Truthy: everything else

Used constantly for API responses: `if response_data: ...`

### for loops
```python
for i in range(5):        # 0 1 2 3 4
for name in ["Ali", "Sara"]:
for char in "hello":
for i, name in enumerate(names):   # index + value
```

`range(5)` → `0,1,2,3,4` (stops **before** 5).
`range(1, 5)` → `1,2,3,4`
`range(1, 10, 2)` → `1,3,5,7,9`

**Rule:** the `for` handles the counter. **Never** manually `+= 1` inside a `for`.

### while loops
```python
count = 0
while count < 5:
    print(count)
    count += 1     # MUST change something
```

- `break` → exit loop
- `continue` → skip to next iteration
- Infinite loop? `Ctrl+C` in the terminal.

---

## 6. Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

greet("Umer")             # "Hello, Umer"
greet("Umer", "Salam")    # "Salam, Umer"
```

- `def` = define
- `name` = **parameter** (placeholder)
- `"Umer"` = **argument** (actual value)
- `return` sends a value back

### return vs print — CRITICAL
```python
def add_print(a, b):
    print(a + b)     # shows on screen, returns None

def add_return(a, b):
    return a + b     # sends value back

x = add_print(2, 3)   # x is None
y = add_return(2, 3)  # y is 5
```

**A function with no `return` returns `None`.**

### Default arguments
Defaults must come **after** non-default parameters.

### Scope
Variables created inside a function stay inside. To get a value out, `return` it.

```python
def f():
    x = 10
    return x

f()
print(x)   # ❌ NameError
```

---

## 7. Git Routine (daily)

```bash
git status
git add .
git commit -m "Day X: short description"
git push
```

Mental model:
```
work on files
↓
git status   = see what changed
↓
git add .    = stage changes
↓
git commit   = save local checkpoint
↓
git push     = send to GitHub
```

Repo: `https://github.com/umershahid21/30-days-python-web.git`
Local: `D:\30-days-python-web`
Branch: `main`

---

## 8. Style Rules (PEP 8)

- `snake_case` for variables/functions
- Spaces around operators: `marks >= 90`, not `marks >=90`
- No space between function name and `(`: `print(x)`, not `print (x)`
- 4-space indentation
- Meaningful names over short names

---

## 9. Day 1 Concepts to Remember Long-Term

1. `input()` → always `str`. Cast before math.
2. `/` returns float, `//` floor, `%` remainder.
3. `=` assigns, `==` compares.
4. Function with no `return` → `None`.
5. `for` handles its own counter. No manual `+= 1`.
6. Falsy values: `""`, `0`, `[]`, `{}`, `None`, `False`.
7. F-string: `f"{var}"` — cleanest way to format output.