# Write day-02/file_handling.py:

# Part A — Write

# Use "w" mode to create a file called day-02/notes.txt and write 3 lines into it. Each line should be a sentence about something you learned today (any topic).
# Add \n at the end of each line so they're actually on separate lines.

# Part B — Read

# Open the same file in "r" mode and read it in two ways:
# First, read() it and print the whole content.
# Then, loop line-by-line and print each line with its line number (start at 1), stripped of the \n.

# Part C — Append

# Open the file in "a" mode and add 2 more lines.
# Re-read the file and print it, to confirm your new lines are there.

# Part D — Count
# Read the file and print the total number of lines.

# Rules:
# Use with for every file operation.
# Use f-strings when writing lines.
# snake_case.
# Run the script twice. Observe what happens to notes.txt on the second run. Write a one-line comment at the bottom explaining what you noticed.
# Hint to think about: which mode overwrites, which appends, and what happens if you read a file that has data from both runs?


with open("day-02/notes.txt", "w") as f:
    f.write("Today I learned about file handling in Python.\n")
    f.write("I practiced reading and writing files using different modes.\n")
    f.write("I also learned how to count lines in a file.\n")

with open("day-02/notes.txt", "r") as f:
    content=f.readlines()
    print(f"Content of the file: {content}")

with open("day-02/notes.txt", "r") as f:
    print("reading line by line:")
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")

with open("day-02/notes.txt", "a") as f:
    f.write("I learned about the importance of using 'with' for file operations.\n")
    f.write("I also learned how to use f-strings for writing lines.\n")

with open("day-02/notes.txt", "r") as f:
    content=f.readlines()
    print(f"Content of the file after appending: {content}")
    print(f"Total number of lines: {len(content)}")

# Running the script twice gives 5 lines each time — "w" mode wipes the file
# at the start of every run, so the previous run's data is gone before "a" appends.



