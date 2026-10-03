# Rewrite each of these as a comprehension in day-02/comprehensions.py. Put the original loop as a comment above each comprehension so you can compare.

# 1. Squares of 1–10

# squares = []
# for n in range(1, 11):
#     squares.append(n * n)

# 2. Only even numbers from 1–20

# evens = []
# for n in range(1, 21):
#     if n % 2 == 0:
#         evens.append(n)

# 3. Uppercase every name

# names = ["ali", "sara", "umer", "hina"]
# upper = []
# for name in names:
#     upper.append(name.upper())

# 4. Length of each word
# words = ["hi", "hello", "hey", "goodbye"]
# lengths = []
# for w in words:
#     lengths.append(len(w))

# 5. Only names longer than 3 characters (filter + transform)
# names = ["ali", "sara", "umer", "hina", "bo"]
# long_names = []
# for name in names:
#     if len(name) > 3:
#         long_names.append(name.capitalize())

# 6. Dict comprehension — name → length
# names = ["ali", "sara", "umer"]
# name_lengths = {}
# for name in names:
#     name_lengths[name] = len(name)
# 7. Set comprehension — unique word lengths

# words = ["hi", "hello", "hey", "goodbye"]
# unique_lengths = set()
# for w in words:
#     unique_lengths.add(len(w))
# Write all 7. For each one, add a comment on the same line saying what you expect the output to be. Then run it and check if your prediction was right. Report any surprises.

squares=[n*n for n in range(1,11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even=[n for n in range(1,21) if n%2==0] # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
upper=[name.upper() for name in ["ali", "sara", "umer", "hina"]] # ['ALI', 'SARA', 'UMER', 'HINA']
lengths=[len(w) for w in ["hi", "hello", "hey", "goodbye"]] # [2, 5, 3, 7]
long_names=[name.capitalize() for name in ["ali", "sara", "umer", "hina", "bo"] if len(name)>3] # ['Sara', 'Umer', 'Hina']
name_lengths={name:len(name) for name in ["ali", "sara", "umer"]} # {'ali': 3, 'sara': 4, 'umer': 4}
unique_lengths={len(w) for w in ["hi", "hello", "hey", "goodbye"]} # {2, 3, 5, 7}

print(squares)
print(even)
print(upper)
print(lengths)
print(long_names)
print(name_lengths)
print(unique_lengths)