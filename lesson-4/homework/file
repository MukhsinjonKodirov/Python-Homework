# 1.
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

sample_dict = {2: 30, 1: 10, 3: 20}
print("Ascending:", sort_dict_by_value(sample_dict))
print("Descending:", dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True)))

# 2. Add a Key to a Dictionary
def add_key_to_dict(d, key, value):
    d[key] = value
    return d

sample_dict = {0: 10, 1: 20}
sample_dict = add_key_to_dict(sample_dict, 2, 30)
print("Updated Dictionary:", sample_dict)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatenated_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", concatenated_dict)

# 4. Generate a Dictionary with Squares
def generate_squares(n):
    return {x: x*x for x in range(1, n+1)}

print("Squares Dictionary (n=5):", generate_squares(5))

# 5. Dictionary of Squares (1 to 15)
print("Squares Dictionary (1 to 15):", generate_squares(15))


# Set Exercises

# 1. Create a Set
my_set = {1, 2, 3, 4, 5}
print("Created Set:", my_set)

# 2. Iterate Over a Set
print("Iterating Over Set:")
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
my_set.add(6)
my_set.update([7, 8, 9])
print("Updated Set:", my_set)

# 4. Remove Item(s) from a Set
my_set.remove(3)  # Raises error if element is not found
my_set.discard(10)  # No error if element is not found
print("Set after removals:", my_set)

# 5. Remove an Item if Present in the Set
if 2 in my_set:
    my_set.remove(2)
print("Set after conditional removal:", my_set)

