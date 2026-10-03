# Part A — Write code in day-02/modules_demo.py:
# Import math. Print sqrt(144) and pi using the math. prefix.
# Import sqrt and factorial directly from math and use them without the prefix.
# Import random. Print a random integer between 1 and 100 (look up random.randint).
# Import datetime. Print today's date (search: datetime.date.today()).
# Import json. Take a Python dict, convert it to a JSON string with json.dumps(...), and print the string. Then convert it back to a dict with json.loads(...) and print the dict.

# Part B — Setup venv (do this in the terminal, not in the .py file):
# In your terminal, from D:\30-days-python-web, run:
# powershell
# python -m venv .venv
# Activate it:
# powershell
# .venv\Scripts\Activate.ps1
# Confirm (.venv) shows in your prompt.

# Run:
# powershell
# pip list
# You should see only the default packages (pip, setuptools) — none of the ones you may have installed globally.
# Install requests:

# powershell
# pip install requests
# Run pip freeze > requirements.txt to save it.
# Open requirements.txt — you should see requests (plus its dependencies) listed.
# Deactivate with deactivate.
# Run git status — confirm .venv/ is not showing as untracked (it should be ignored by your .gitignore).

import math


print(f"square root of 144: {math.sqrt(144)}")
print(f"pi: {math.pi}")

from math import sqrt, factorial
print(f"square root of 144 using direct import: {sqrt(144)}")
print(f"factorial of 5: {factorial(5)}")

import random
print(f"Random integer between 1 and 100: {random.randint(1, 100)}")

import datetime
print(f"Today's date: {datetime.date.today()}")

import json
data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")
parsed_data = json.loads(json_string)
print(f"Parsed dict: {parsed_data}")