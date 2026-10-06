# Day 3 — OOP Fundamentals & Advanced

Repo: `30-days-python-web` · Branch: `main`

---

## 1. Classes and Objects

A **class** is a blueprint. An **object** (instance) is something built from that blueprint.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Umer", 24)
print(user.name)   # "Umer"
```

- Class names use **PascalCase**: `User`, `BankAccount`, `Book`.
- Variables, methods, and attributes use **snake_case**.
- Creating an object: `User("Umer", 24)` — Python calls `__init__` automatically.

---

## 2. `__init__` and `self`

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

- **`__init__`** runs automatically when an object is created. Called the *initializer* (people often call it "constructor").
- **`self`** is the object being created. Python passes it silently — you never pass it yourself.
- **`self.name = name`** stores the value on that specific object (an *instance attribute*).
- `self` is just a name — but **always use `self`**. Don't be clever.

---

## 3. Instance vs Class Attributes

**Instance attributes** — unique per object:
```python
class User:
    def __init__(self, name):
        self.name = name    # instance attribute
```

**Class attributes** — shared by all instances, defined outside `__init__`:
```python
class User:
    species = "human"       # class attribute

    def __init__(self, name):
        self.name = name
```

**The shadowing gotcha:**
```python
User.species = "mammal"     # changes it for ALL users
u1.species = "alien"        # creates an INSTANCE attribute on u1 only
                            # u1 shadows the class attribute
```

**When to use which:**
- Instance → value differs per object (name, age, email)
- Class → same for all objects (default, constant, counter)

---

## 4. Method Types

| Type | First arg | Decorator | Called on | Can access |
|---|---|---|---|---|
| Instance | `self` | none | `obj.method()` | instance + class attributes |
| Class | `cls` | `@classmethod` | `Class.method()` | class attributes only |
| Static | none | `@staticmethod` | `Class.method()` or `obj.method()` | neither |

**Instance method:**
```python
def increment(self):
    self.value += 1
```

**Class method** (alternate constructors, class-level logic):
```python
@classmethod
def from_string(cls, text):
    obj = cls()
    obj.value = int(text)
    return obj
```

**Static method** (utility function that lives with the class):
```python
@staticmethod
def is_positive(n):
    return n > 0
```

**Rule of thumb:**
- Default to instance methods.
- `@classmethod` for alternate constructors or factory patterns.
- `@staticmethod` for helpers that don't need class or instance state.

---

## 5. Inheritance & `super()`

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run parent's __init__ first
        self.breed = breed
```

- `Dog(Animal)` → Dog **inherits** from Animal.
- `super()` calls the parent's version of a method.
- Prefer `super()` over `Animal.__init__(...)` — handles multiple inheritance correctly, and doesn't hard-code the parent name.

**The classic mistake:**
```python
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed          # ← forgot super().__init__(name)
```

Result: `AttributeError: 'Dog' object has no attribute 'name'`.
**The parent's `__init__` never ran, so `self.name` was never set.**

**Overriding:**
```python
class Car(Vehicle):
    def info(self):
        return f"{super().info()} with {self.doors} doors"
```
Use `super().method()` to extend the parent's behavior instead of fully replacing it.

---

## 6. `isinstance` and the "IS-A" test

```python
d = Dog("Rex", "Lab")
isinstance(d, Dog)       # True
isinstance(d, Animal)    # True   ← every Dog IS an Animal
isinstance(Animal("x"), Dog)     # False  ← not every Animal is a Dog
```

**When to use inheritance:**
- Only when the child **IS-A** type of the parent: `Dog IS-A Animal`, `SavingsAccount IS-A BankAccount`.
- If the relationship is **HAS-A**, use composition: `Car HAS-A Engine` → `Car` should have `self.engine`, not inherit from `Engine`.

Every framework base class works this way — `User(BaseModel)`, `Post(models.Model)`, etc.

---

## 7. Encapsulation — `_`, `@property`, setters

### The problem
Without protection, outside code can set anything:
```python
account.balance = -5000     # nonsense, but Python allows it
account.balance = "hello"   # now it's a string, object is broken
```

### Step 1 — `_` convention
```python
self._balance = balance     # "_" means "internal, don't touch"
```
A **signal** to other programmers — not enforced by Python.

### Step 2 — `@property` (read-only)
```python
@property
def balance(self):
    return self._balance
```
- Access as an attribute: `account.balance` (no parentheses).
- Python runs the method behind the scenes.
- Now `balance` exists as a public name, but is **read-only**.

**Error if you try to write:** `AttributeError: property 'balance' ... has no setter`.

### Step 3 — `@balance.setter` (validation on write)
```python
@balance.setter
def balance(self, value):
    if value < 0:
        raise ValueError("Balance cannot be negative")
    self._balance = value
```
- Both methods share the same name (`balance`).
- The decorator `@balance.setter` tells Python "this is the setter for `balance`".
- Now external writes go through **your** validation.

### Computed property
```python
@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"
```
Looks like data, computed on demand. No storage, no staleness. Change `first_name`, `full_name` updates automatically.

### Mental model
| Code | Meaning |
|---|---|
| `self.balance` | public — anyone can read/write |
| `self._balance` | internal — convention says don't touch |
| `@property` | read-only public access |
| `@property` + `@x.setter` | read/write with validation |

**Don't over-engineer.** Start with plain public attributes. Add `_` + `@property` only when you need validation or computed values.

---

## 8. Dunder Methods

Each dunder is a hook into Python syntax:

```
print(obj)              →  obj.__str__()
repr(obj) / REPL        →  obj.__repr__()
obj1 == obj2            →  obj1.__eq__(obj2)
len(obj)                →  obj.__len__()
```

You don't call them directly — Python calls them for you.

### `__str__` and `__repr__`
```python
def __str__(self):
    return f"{self.title} by {self.author}"          # human-friendly

def __repr__(self):
    return f"Book(title={self.title!r}, author={self.author!r})"  # unambiguous
```
- `__str__` → **end user** output (via `print`).
- `__repr__` → **developer** output (REPL, logs). Ideally something you could paste back to rebuild the object.
- `!r` in f-strings means "use `repr()` for this value" → adds quotes around strings.
- **If only one:** write `__repr__`. It's the fallback for `__str__`.

### `__eq__`
```python
def __eq__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return self.x == other.x and self.y == other.y
```
- Without `__eq__`, `==` compares **identity** (memory address). `Point(1,2) == Point(1,2)` → `False`.
- With it → `True` if your criteria match.
- **`NotImplemented` vs `False`:** `NotImplemented` says "I don't know how to compare — let Python try the other object's `__eq__`". `False` says "these are not equal." For type mismatches, `NotImplemented` is correct.
- When you define `__eq__`, you should also define `__hash__` (otherwise objects become unhashable). Skip for now — just know it exists.

### `__len__`
```python
def __len__(self):
    return len(self.songs)
```
- `len(playlist)` calls this.
- **Bonus:** an object with `__len__` returning `0` is **falsy** in an `if`. (`if empty_playlist:` → skipped.)

---

## 9. Key Gotchas (Day 3)

1. **Forgot `super().__init__()`** → parent attributes never set → `AttributeError` on access.
2. **`@property` alone is read-only.** Add `@x.setter` to allow writes.
3. **Setter must have the same name as the property.** `@balance.setter` above `def balance(self, value):`.
4. **Changing a class attribute on an instance** creates an instance-level shadow — doesn't touch the class.
5. **`__eq__` returns `NotImplemented`, not `False`** when the type can't be compared.
6. **`__eq__` without `__hash__`** makes objects unhashable (can't go in sets or as dict keys).
7. **`isinstance` follows inheritance:** a `Dog` is also an `Animal`. But not the reverse.
8. **Use inheritance for "IS-A", composition for "HAS-A".**

---

## 10. Day 3 Files Created

```
day-03/
├── classes_basics.py      # class, __init__, self, instance vs class attrs
├── methods.py             # instance / @classmethod / @staticmethod
├── inheritance.py         # inheritance, super(), isinstance
├── encapsulation.py       # _, @property, setters with validation
├── dunder_methods.py      # __str__, __repr__, __eq__, __len__
└── notes.md               # this file
```