# =====================================================================
# Part A — __str__ and __repr__
# =====================================================================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"


b = Book("The Hobbit", "Tolkien")
print(b)        # Uses __str__ -> The Hobbit by Tolkien
print(repr(b))  # Uses __repr__ explicitly -> Book(title='The Hobbit', author='Tolkien')

# Comment:
# What would print(b) show if you only had __repr__ and no __str__?
# Answer:
# It would fall back to __repr__ and output:
# "Book(title='The Hobbit', author='Tolkien')"
# In Python, if __str__ is not defined on an object, print() and str() fall
# back to __repr__ as a default readable representation.


# =====================================================================
# Part B — __eq__
# =====================================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


# Tests:
print(Point(1, 2) == Point(1, 2))  # True
print(Point(1, 2) == Point(3, 4))  # False
print(Point(1, 2) == "hello")       # False (does not crash)

# Comment:
# Without __eq__, what would Point(1, 2) == Point(1, 2) return, and why?
# Answer:
# It would return False.
# Without __eq__, Python falls back to object identity comparison (`is`)
# inherited from the base `object` class, comparing memory addresses (id).
# Because each Point(1, 2) is a newly allocated instance at a distinct memory
# address, they are not identical objects and thus evaluate to False.


# =====================================================================
# Part C — __len__
# =====================================================================

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


# Create a playlist with 3 songs
playlist = Playlist(["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"])
print("Playlist length:", len(playlist))  # 3

# Create an empty playlist
empty_playlist = Playlist([])
print("Empty playlist length:", len(empty_playlist))  # 0

# Bonus: test `if playlist:` with the empty one
if empty_playlist:
    print("Empty playlist is truthy")
else:
    print("Empty playlist is falsy")  # Prints this!
# Explanation: When an object has no __bool__ method defined, Python falls
# back to __len__ for truth value testing. If __len__() returns 0, the object
# evaluates to False (is falsy).


# =====================================================================
# Part D — Combine
# =====================================================================

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return f"Team {self.name} ({len(self.members)} members)"

    def __repr__(self):
        return f"Team(name={self.name!r}, members={self.members!r})"

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return self.name == other.name and self.members == other.members

    def __len__(self):
        return len(self.members)


# Create two identical teams and compare them
team1 = Team("Avengers", ["Iron Man", "Thor", "Captain America"])
team2 = Team("Avengers", ["Iron Man", "Thor", "Captain America"])

print("team1 == team2:", team1 == team2)  # True

# Print the team and its length
print(team1)               # Team Avengers (3 members)
print("repr:", repr(team1))# Team(name='Avengers', members=['Iron Man', 'Thor', 'Captain America'])
print("Length:", len(team1)) # 3

