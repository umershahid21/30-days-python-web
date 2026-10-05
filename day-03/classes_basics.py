# Part A — Basic class

# Define a class Book with __init__ accepting title and author. Store both as instance attributes.
# Create two Book objects with different titles and authors.
# Print each book's title and author using dot notation.

# Part B — Instance vs class attribute

# Add a class attribute format = "paperback" to Book.
# Print Book.format and book1.format.
# Change Book.format to "hardcover". Print book1.format and book2.format — what do you see? Write a comment explaining it.
# Now set book1.format = "ebook". Print book1.format and book2.format. Write a comment explaining why they differ.

# Part C — Defaults + validation in __init__

# Extend Book.__init__ to accept an optional pages parameter with a default value of 0.
# Inside __init__, if pages is 0 or negative, store self.pages = "unknown" instead.
# Create a book with pages, and a book without pages. Print both.

# Part D — A method that uses self

# Add a method description(self) to Book that returns a string like:
# "The Hobbit by Tolkien (paperback, 310 pages)".
# Call it on both books and print the results.

# Rules:

# PascalCase for class names (Book, User, not book or user).
# snake_case for variables, methods, attributes.
# Use f-strings.
# No inheritance, no @property, no dunder magic beyond __init__ yet.


class Book:
    format = "paperback"


    def __init__(self,title,author,pages=0):
        if pages <= 0:
            self.pages = "unknown"
        else:
            self.pages = pages
        self.title=title
        self.author=author

    def description(self):
        return f"{self.title} by {self.author} ({self.format}, {self.pages} pages)"

book1 = Book("The Hobbit","Tolkien")
book2 = Book("1984","Orwell")
book3 = Book("The Hobbit", "Tolkien", 310)
print(book1.title,book1.author)
print(book2.title,book2.author)
print(book3.title,book3.author)

print(Book.format)
print(book1.format)

Book.format="hardcover"
print(book1.format)
print(book2.format) #both book1 and book2 will print "hardcover" because they are accessing the class attribute format, which was changed to "hardcover".

book1.format="ebook"
print(book1.format)
print(book2.format) #book1 and book2 differ because book1 has its own instance attribute format set to "ebook", while book2 still accesses the class attribute format, which is "hardcover".

print(book1.description())
print(book2.description())
print(book3.description())