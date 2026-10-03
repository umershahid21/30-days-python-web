# Part A — Lists

# Create a list of 5 fruits.

# Append a fruit, insert one at index 1, remove one by name.
# Print the list, its length, and whether "apple" is in it.
# Print the last item using negative indexing.
# Loop through and print each fruit with its index (use enumerate).

# Part B — Tuples

# Create a tuple with (latitude, longitude).
# Unpack it into lat, lon and print each.

# Part C — Dictionaries

# Create a user dict with at least name, age, city.
# Add an email key.
# Print the user's name using .get().
# Print a missing key using .get() with a default value of "N/A".
# Loop through the dict and print key: value for every entry.

# Part D — Sets

# Create a list with duplicates: [1, 1, 2, 2, 3, 4, 4, 5].
# Convert to a set and back to a list to remove duplicates.
# Print the result.
# Create two sets, print their union and intersection.

# Rules:
# snake_case, f-strings where useful.
# Comments at the top of each part.
# No comprehensions yet — we do those next. Use regular loops.


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.append("pomegranate")
fruits.insert(1, "kiwi")
fruits.remove("banana")
print(fruits)

print(f"Length of fruits list: {len(fruits)}")
print(f"Last fruit: {fruits[-1]}")
print(f"Is 'apple' in the list? {'apple' in fruits}")

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

latitude, longitude = (34.0522, -118.2437)
print (f"latitude: {latitude}, longitude: {longitude}")


user = {"name": "Umer", "age": 24, "city": "Karachi"}
user["email"]="umer@example.com"
print(f"User's name: {user.get('name')}")
print(f"User's phone: {user.get('phone', 'N/A')}")

for key,value in user.items():
    print(f"key: {key}, value: {value}")


list_with_duplicates = [1, 1, 2, 2, 3, 4, 4, 5]
unique_set=set(list_with_duplicates)
list_now=list(unique_set)
print(f"List after removing duplicates: {list_now}")

set1={1,2,3,4}
set2={3,4,5,6}
print(f"union: {set1|set2}")
print(f"intersection: {set1&set2}")

