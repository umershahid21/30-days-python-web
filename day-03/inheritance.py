# Your question
# Write day-03/inheritance.py:

# Part A — Basic inheritance
# Class Vehicle with __init__(self, brand) storing self.brand, and a method info(self) that returns "Vehicle: {brand}".
# Class Car(Vehicle) with no new code — just pass.
# Create a Car("Toyota"). Print car.brand and car.info(). Confirm both come from Vehicle.

# Part B — Override a method
# Add a method info(self) to Car that returns "Car: {brand}" — completely replacing Vehicle's version.
# Create a Car("Toyota") and a Vehicle("Generic"). Print both info() results. Confirm they differ.
# Part C — super().__init__()

# Add __init__(self, brand, doors) to Car. It should call super().__init__(brand) first, then set self.doors = doors.
# Create Car("Toyota", 4). Print brand and doors.
# Now temporarily remove the super().__init__(brand) line and run again. Paste the error message you get. Then put it back.

# Part D — Extending with super() in a method
# In Car.info(), instead of fully replacing Vehicle's version, call super().info() and append the doors info:
# python
# def info(self):
#     return f"{super().info()} with {self.doors} doors"
# Print the result. It should show "Vehicle: Toyota with 4 doors".

# Part E — isinstance
# Create car = Car("Toyota", 4) and vehicle = Vehicle("Generic").
# Print isinstance(car, Car) and isinstance(car, Vehicle).
# Print isinstance(vehicle, Car).
# Write a one-line comment explaining why isinstance(car, Vehicle) is True but isinstance(vehicle, Car) is False.

# Rules:
# PascalCase for classes.
# super() — not the parent class name.
# One blank line between methods inside a class, two blank lines between top-level class definitions.


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Vehicle: {self.brand}"

class Car(Vehicle):

    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def info(self):
        return f"{super().info()} with {self.doors} doors"
        # pass
car1=Car("Toyota",4)
vehicle=Vehicle("Generic")
print(vehicle.info())
print(car1.info())
print(car1.brand)
print(car1.doors)

# #PS D:\30-days-python-web> python -u "d:\30-days-python-web\day-03\inheritance.py"
# Vehicle: Generic
# Traceback (most recent call last):
#   File "d:\30-days-python-web\day-03\inheritance.py", line 56, in <module>
#     print(car1.info())
#           ~~~~~~~~~^^
#   File "d:\30-days-python-web\day-03\inheritance.py", line 51, in info
#     return f"Car: {self.brand}"
#                    ^^^^^^^^^^
# AttributeError: 'Car' object has no attribute 'brand'

print(isinstance(car1, Car))
print(isinstance(car1, Vehicle))
print(isinstance(vehicle, Car))

# isinstance(car1, Vehicle) is True because car1 is an instance of Car, and Car inherits from Vehicle.
# isinstance(vehicle, Car) is False because vehicle is an instance of Vehicle, and Vehicle does not inherit from Car.