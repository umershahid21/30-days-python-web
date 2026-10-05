    # Write day-03/methods.py:

    # Part A — Instance method
    # Class Counter with __init__ storing self.value = 0.
    # Instance method increment(self) that adds 1 to self.value.
    # Create a counter, call increment() three times, print counter.value. Expect 3.

    # Part B — Class method
    # Add a class attribute total_counters = 0 to Counter.
    # In __init__, increment Counter.total_counters every time a new Counter is created.
    # Add a @classmethod called get_total(cls) that returns cls.total_counters.

    # Create 3 counters, print Counter.get_total().
    # Part C — Class method as alternate constructor
    # Add a @classmethod from_string(cls, text) to Counter that takes a string like "5" and returns a new Counter with self.value set to that number.

    # Test: c = Counter.from_string("5") then print(c.value).
    # Hint: inside the classmethod, you need to create the object first, then set the value. Something like:

    # python
    # obj = cls()
    # obj.value = int(text)
    # return obj
    # Part D — Static method

    # Add a @staticmethod is_positive(n) to Counter that returns True if n > 0, else False.
    # Call it on the class: Counter.is_positive(5) and Counter.is_positive(-3).
    # Call it on an instance too: counter.is_positive(10) — same result.

    # Part E — Comment
    # At the bottom of the file, write two comments:
    # One explaining when you'd choose @classmethod over an instance method.
    # One explaining when you'd choose @staticmethod over a @classmethod.
    # Answer in your own words — I want to see your understanding, not a copy of mine.

class Counter:

    total_counters = 0

    def __init__(self):
        self.value = 0
        Counter.total_counters += 1


    def increment(self):
        self.value += 1


    @classmethod
    def get_total(cls):
        return cls.total_counters
        
    @classmethod
    def from_string(cls, text):
        obj = cls()
        obj.value = int(text)
        return obj

    @staticmethod
    def is_positive(n):
        return n > 0
        



counter1 = Counter()
counter1.increment()
counter1.increment()
counter1.increment()
print(counter1.value) # Expect 3

counter2 = Counter()
counter3 = Counter()


c = Counter.from_string("5")
print(Counter.get_total()) # Expect 3
print(counter1.value) # Expect 3
print(c.value) # Expect 5
print(Counter.is_positive(5)) # Expect True
print(Counter.is_positive(-3)) # Expect False
print(c.is_positive(10)) # Expect True
#class method is used when class-level data or behavior is needed, such as creating instances in a specific way or accessing class attributes. Instance methods are used when you need to work with individual object data.
#static method is used when you want to perform a function that doesn't depend on class or instance data. It's a utility function that can be called on the class or an instance, but it doesn't modify or access any class or instance attributes.