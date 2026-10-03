# Day 2 — Data Structures & Tooling

Repo: `30-days-python-web` · Branch: `main`

---

## 1. Lists — ordered, changeable, allow duplicates

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
empty = []
```

**Indexing & slicing** (same rules as strings):
```python
fruits[0]      # "apple"     (first)
fruits[-1]     # "cherry"    (last)
fruits[1:3]    # ["banana", "cherry"]  (start inclusive, stop exclusive)
```

**Common methods:**
```python
fruits.append("date")          # add to end
fruits.insert(1, "mango")      # insert at index
fruits.remove("banana")        # remove by value (first match)
fruits.pop()                   # remove & return last item
fruits.pop(0)                  # remove & return index 0
fruits.sort()                  # sort in place
fruits.reverse()               # reverse in place
len(fruits)                    # length
"apple" in fruits              # True/False
```

**`append` vs `+`:**
```python
a = [1, 2]
a.append(3)      # modifies in place → a = [1, 2, 3]
b = a + [4, 5]   # returns new list → b = [1, 2, 3, 4, 5], a unchanged
```

**Lists are mutable — copy gotcha:**
```python
a = [1, 2, 3]
b = a            # b is the SAME list, not a copy
b.append(4)
print(a)         # [1, 2, 3, 4]  ← a changed too!

b = a.copy()     # ✅ actual copy (also: list(a) or a[:])
```

---

## 2. Tuples — ordered, unchangeable, allow duplicates

```python
coordinates = (10, 20)
rgb = (255, 0, 0)
single = (5,)          # ← comma required for 1-element tuple
```

- Indexing/slicing work like lists.
- **No** `append`, `remove`, `pop`.
- Use tuples for **things that shouldn't change**: coordinates, RGB, DB IDs.

**Unpacking** (very common in real code):
```python
x, y = (10, 20)
name, age, city = ("Umer", 24, "Lahore")
```

**When to use list vs tuple:**
- List → collection that will change (to-do list, API results)
- Tuple → fixed group of related values (x/y, RGB, config pair)

---

## 3. Dictionaries — key → value pairs

```python
user = {
    "name": "Umer",
    "age": 24,
    "city": "Lahore"
}
```

**Access & modify:**
```python
user["name"]                 # "Umer"
user["age"] = 25             # update
user["email"] = "..."        # add new key

user.get("name")             # "Umer"
user.get("phone")            # None  ← safe, no crash
user.get("phone", "N/A")     # "N/A" ← default value

"name" in user               # True
user.keys()                  # dict_keys(['name', 'age', 'city'])
user.values()                # the values
user.items()                 # pairs as (key, value) tuples
```

**Why `.get()` matters:**
```python
user["phone"]           # ❌ KeyError — crashes if missing
user.get("phone")       # ✅ returns None, no crash
```
API data often has missing keys. `.get()` is the safety net. Used constantly in n8n and API work.

**Dicts are mutable too** — same copy gotcha as lists:
```python
a = {"x": 1}
b = a
b["y"] = 2
print(a)   # {"x": 1, "y": 2}  ← a changed too
```

---

## 4. Sets — unordered, unique values only

```python
numbers = {1, 2, 3, 3, 3}
print(numbers)   # {1, 2, 3}  ← duplicates removed

empty = set()    # ← NOT {} — that's an empty dict!
```

**Methods:**
```python
numbers.add(4)         # add
numbers.remove(1)      # remove (KeyError if missing)
numbers.discard(99)    # remove if present, no error if not

a = {1, 2, 3}
b = {3, 4, 5}
a | b    # union        → {1, 2, 3, 4, 5}
a & b    # intersection → {3}
a - b    # difference   → {1, 2}
```

**Most common use — dedupe a list:**
```python
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))   # [1, 2, 3]
```
Read right-to-left: list → set (dupes auto-dropped) → back to list.
Sets have **no order and no indexing** — `numbers[0]` doesn't work.

---

## 5. The "for X in Y" pattern (the concept that finally clicked)

**The rule:**
```python
for SOMETHING in COLLECTION:
```
- `SOMETHING` is a **name you invent**. It can be anything.
- `COLLECTION` is anything iterable.
- Python hands you **one item per iteration** and puts it in `SOMETHING`.

| What you loop over | What you get each turn |
|---|---|
| `range(3)` | `0`, `1`, `2` |
| `["a", "b"]` | `"a"`, `"b"` |
| `{"name": "Umer", "age": 24}` | `"name"`, `"age"` (keys) |
| `{"name": "Umer"}.items()` | `("name", "Umer")` pairs |
| `enumerate(["a", "b"])` | `(0, "a")`, `(1, "b")` pairs |
| `"hello"` | `"h"`, `"e"`, `"l"`, `"l"`, `"o"` |

**Unpacking in the `for` line:**
```python
for i, fruit in enumerate(fruits):       # unpacks 2 values
for key, value in user.items():          # unpacks 2 values
for a, b, c in [(1,2,3), (4,5,6)]:       # unpacks 3 values
```

**Dict looping — two ways, both work:**
```python
for key in user:
    print(key, user[key])

for key, value in user.items():          # ← preferred
    print(f"{key} = {value}")
```

**Line numbering with enumerate:**
```python
for i, line in enumerate(f, start=1):    # start=1 for line numbers starting at 1
    print(f"{i}: {line.strip()}")
```

**Rule:** the `for` handles the counter. **Never** manually `+= 1` inside a `for`.

---

## 6. Comprehensions — loop + build-in-one-line

**Read right-to-left:**
```python
[n * n        for n in numbers]
 ↑              ↑
 what to put   where the values come from
 in the new
 list
```

**Basic:**
```python
numbers = [1, 2, 3, 4, 5]
squared = [n * n for n in numbers]       # [1, 4, 9, 16, 25]
```

**With filter:**
```python
evens = [n for n in range(1, 21) if n % 2 == 0]
```

**With transform + filter:**
```python
long_names = [name.capitalize() for name in names if len(name) > 3]
```

**Dict comprehension:**
```python
name_lengths = {name: len(name) for name in names}
# {"ali": 3, "sara": 4, "umer": 4}
```

**Set comprehension:**
```python
unique_lengths = {len(w) for w in words}
# {2, 3, 5, 7}
```

**When NOT to use one:** if it's not readable at a glance, use a normal loop. Don't nest ternaries inside comprehensions.

---

## 7. File Handling

### The `with` statement (always use this)
```python
with open("data.txt", "r") as f:
    content = f.read()
# file auto-closed here, even if an error occurs
```
Never use bare `open()` without `with` in real code.

### Modes
| Mode | Meaning | Behavior |
|---|---|---|
| `"r"` | read | default. **Errors if file doesn't exist.** |
| `"w"` | write | **Overwrites.** Creates if missing. |
| `"a"` | append | Adds to end. Creates if missing. Never overwrites. |
| `"x"` | create | Creates file, errors if it exists. |
| `"rb"` / `"wb"` | binary | images, PDFs, etc. |

**`"w"` is dangerous** — it wipes the file the moment you open it.

### Reading — three ways
```python
with open("data.txt", "r") as f:
    content = f.read()          # one string with everything

with open("data.txt", "r") as f:
    lines = f.readlines()       # list of lines (each ends with \n)

with open("data.txt", "r") as f:
    for line in f:              # line by line (best for big files)
        print(line.strip())
```

**`.strip()` matters** — each line keeps its `\n` unless you strip it.

### Writing
```python
with open("output.txt", "w") as f:
    f.write(f"Name: {name}\n")   # write() does NOT add a newline
    f.write(f"Age: {age}\n")
```

### Appending
```python
with open("log.txt", "a") as f:
    f.write("new entry\n")       # repeated runs add to the file
```

**Gotcha observed:** if a file has a `"w"` block and later an `"a"` block, the `"w"` wipes everything at the start of each run — so runs 1 and 2 produce identical output. To accumulate across runs, change the first block to `"a"`.

### Errors you'll hit
```python
with open("nope.txt", "r") as f:
    ...
# FileNotFoundError: [Errno 2] No such file or directory: 'nope.txt'
```

---

## 8. Exceptions (try / except / finally)

**The structure:**
```python
try:
    # risky code
except SpecificError:
    # handle it
except AnotherError:
    # handle it
finally:
    # always runs (optional)
```

**Basic:**
```python
try:
    age = int(input("Age: "))
    print(f"You are {age}")
except ValueError:
    print("That wasn't a valid number.")
```

**Multiple except clauses — order matters (first match wins):**
```python
try:
    result = a / b
except ValueError:
    print("Please enter whole numbers.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

**Catching the error object:**
```python
try:
    a = int("hello")
except ValueError as e:
    print(f"Error: {e}")
```
`as e` gives you the actual exception object. `str(e)` shows the message. Useful for logging.

**`else` and `finally`:**
```python
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    print("Opened successfully.")
    f.close()
finally:
    print("This runs no matter what.")
```
- `else` — runs only if **no exception** occurred
- `finally` — runs **always**

**Common exceptions:**
| Exception | When |
|---|---|
| `ValueError` | `int("hello")` |
| `TypeError` | `"a" + 1` |
| `ZeroDivisionError` | `10 / 0` |
| `KeyError` | `d["missing"]` |
| `IndexError` | `[1, 2][5]` |
| `FileNotFoundError` | opening a missing file |
| `AttributeError` | calling a method that doesn't exist |

**Rules:**
- Catch **specific** exceptions, not bare `Exception`.
- Keep the `try` block **small** — only the risky line(s).
- Use `except Exception` only when you genuinely don't know what might fail (e.g. top-level logging).

---

## 9. Modules & Imports

**Import styles:**
```python
import math
math.sqrt(16)              # qualified — safest, clearest

from math import sqrt
sqrt(16)                   # only imports sqrt

from math import sqrt, pi  # multiple names
import math as m
m.sqrt(16)                 # alias
```

**Common built-in modules:**
- `math` — sqrt, pi, ceil, floor, factorial
- `random` — random(), randint(), choice()
- `datetime` — date, datetime, timedelta
- `json` — loads / dumps (JSON parsing — critical for APIs)
- `os` — files, paths, env vars
- `sys` — system, `sys.argv`

**JSON round-trip (used constantly with APIs):**
```python
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)      # dict → JSON string
parsed = json.loads(json_string)    # JSON string → dict
```

**`if __name__ == "__main__":`**
```python
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```
Means: **"only run this if executed directly, not when imported."** Every real Python project uses this pattern.

**Packages:** a folder of modules, usually with an `__init__.py` inside.
```python
from utils.math_helpers import add
```

**Rule:** all imports go at the **top** of the file, before any other code (PEP 8).

---

## 10. pip & requirements.txt

```powershell
pip install requests
pip list
pip freeze > requirements.txt   # save current packages + versions
pip install -r requirements.txt # recreate from file
```

**Why `requirements.txt` matters:** anyone cloning your repo runs `pip install -r requirements.txt` and gets the **exact same** package versions. Essential for sharing projects.

---

## 11. venv (Windows PowerShell workflow)

**The problem:** global installs are shared across all projects → version conflicts.

**The solution:** one isolated environment per project.

```powershell
# From project root
python -m venv .venv

# Activate (PowerShell)
.venv\Scripts\Activate.ps1
# prompt becomes: (.venv) PS D:\30-days-python-web>

# Now pip install goes into .venv, not globally
pip install requests
pip freeze > requirements.txt

# Leave
deactivate
```

**If PowerShell blocks activation:**
```
File ... Activate.ps1 cannot be loaded because running scripts is disabled
```
Fix (once, in PowerShell):
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
`RemoteSigned` = "run local scripts freely; internet scripts must be signed." Standard for devs.

**Rules:**
1. One venv per project.
2. **Never commit `.venv/`** — it's huge.
3. Always activate the venv before running/installing.
4. Recreate from `requirements.txt` anytime.

**Verify venv is being ignored:**
```powershell
git check-ignore .venv
# output: .venv   ← good, Git is honoring .gitignore
```

---

## 12. Key Gotchas (Day 2)

1. **`.get()` vs `[key]`** — `d["missing"]` crashes with `KeyError`. Use `.get()` for unknown keys. Critical for API data.
2. **`"w"` mode wipes the file** — the moment you open it, before writing anything.
3. **`write()` doesn't add newlines** — you add `\n` yourself.
4. **Mutability trap** — `b = a` for lists/dicts means **same object**, not a copy. Use `.copy()`.
5. **Sets have no order and no index** — `{1,2,3}[0]` doesn't work.
6. **`{}` is an empty dict, not an empty set** — use `set()` for an empty set.
7. **Never commit `.venv/` or `__pycache__/`** — both auto-generated, both huge, both in `.gitignore`.
8. **Catch specific exceptions** — bare `except Exception` hides bugs.
9. **PEP 8 spacing** — `x = 5`, `a / b`, `print(x)`, `if marks >= 90`. Spaces around operators, none between function name and `(`.
10. **Imports at the top of the file** — never scattered through the code.

---

## 13. Day 2 Files Created

```
day-02/
├── data_structures.py     # lists, tuples, dicts, sets
├── comprehensions.py      # all 7 comprehension types
├── file_handling.py       # with statement, read/write/append
├── exceptions.py          # try/except/finally
├── modules_demo.py        # math, random, datetime, json
└── notes.md               # this file
```

Also created at repo root:
- `requirements.txt` — pinned dependency list
- `.venv/` — local virtual environment (ignored by Git)