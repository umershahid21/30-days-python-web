# ---------- Version A: unguarded ----------
class BankAccountA:
    def __init__(self, balance=0):
        self.balance = balance    # plain public


account_a = BankAccountA(100)
print("Version A — initial:", account_a.balance)     # 100
account_a.balance = -5000
print("Version A — after -5000:", account_a.balance) # -5000 — nothing stopped it


# ---------- Version B: protected with _ ----------
class BankAccountB:
    def __init__(self, balance=0):
        self._balance = balance   # underscore = "internal"

account_b = BankAccountB(100)
# There is no public `balance` — only `_balance`. That's the point of Version B.
print("Version B — _ access works:", account_b._balance)   # 100


# ---------- Version C: @property (read-only) ----------
class BankAccountC:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance


account_c = BankAccountC(100)
print("Version C — read:", account_c.balance)   # 100 ✅
# account_c.balance = 500      # ❌ AttributeError: can't set attribute
# # Uncomment the line above, run it, PASTE the error, then comment it back out.
#  File "d:\30-days-python-web\day-03\encapsulation.py", line 35, in <module>
#     account_c.balance = 500      # ❌ AttributeError: can't set attribute
#     ^^^^^^^^^^^^^^^^^
# AttributeError: property 'balance' of 'BankAccountC' object has no setter



# ---------- Version D: @property + setter with validation ----------
class BankAccountD:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


account_d = BankAccountD(100)
print("Version D — initial:", account_d.balance)   # 100

account_d.balance = 500
print("Version D — after set to 500:", account_d.balance)   # 500

try:
    account_d.balance = -100
except ValueError as e:
    print(f"Version D — blocked: {e}")   # "Balance cannot be negative"


# ---------- Part E: computed property ----------
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("John", "Doe")
print("Full name:", person.full_name)   # "John Doe"
person.first_name = "New"
print("After rename:", person.full_name)   # "New Doe"