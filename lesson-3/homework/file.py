# 1. Create and Access List Elements
fruits = ["Apple", "Banana", "Cherry", "Orange", "Grapes"]
print(fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50, 60, 70]
middle_index = len(numbers) // 2
extracted = [numbers[0], numbers[middle_index], numbers[-1]]
print(extracted

# 4. Convert List to Tuple
movies = ["Inception", "Interstellar", "Matrix", "Titanic", "Avatar"]
movies_tuple = tuple(movies)
print(movies_tuple)

# 5. Check Element in a List
cities = ["London", "New York", "Paris", "Tokyo", "Berlin"]
print("Paris" in cities)

# 6. Duplicate a List Without Using Loops
numbers = [1, 2, 3, 4, 5]
duplicate_numbers = numbers * 2
print(duplicate_numbers)

# 7. Swap First and Last Elements of a List
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

# 8. Slice a Tuple
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num_tuple[3:8])

# 9. Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "elephant", "lion", "tiger")
print(animals.index("lion")

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

# 12. Find the Length of a List and Tuple
list_example = [10, 20, 30, 40]
tuple_example = (100, 200, 300)
print(len(list_example), len(tuple_example))

# 13. Convert Tuple to List
tuple_numbers = (5, 10, 15, 20, 25)
list_numbers = list(tuple_numbers)
print(list_numbers)

# 14. Find Maximum and Minimum in a Tuple
num_tuple = (11, 22, 33, 44, 55)
print(max(num_tuple), min(num_tuple))

# 15. Reverse a Tuple
words_tuple = ("Python", "is", "fun")
reversed_tuple = words_tuple[::-1]
print(reversed_tuple)

