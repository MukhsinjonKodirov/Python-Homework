# 2. Integer Squares Exercise
n = 5
for i in range(n):
    print(i ** 2)
print()

# 3. Loop-Based Exercises

print("First 10 natural numbers:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Exercise 2: Print the pattern

for i in range(1, 6):
    print(" ".join(str(j) for j in range(1, i + 1)))
print()

# Exercise 3: Sum of all numbers from 1 to n
num = 10
print(f"Sum of numbers from 1 to {num}: {sum(range(1, num + 1))}")
print()

# Exercise 4: Multiplication table

for i in range(1, 11):
    print(2 * i)
print()

# Exercise 5: Display specific numbers from list

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num in [75, 150, 145]:
        print(num)
print()

# Exercise 6: Count digits in a number
num = 75869
print(f"Total digits in {num}: {len(str(num))}")
print()

# Exercise 7: Reverse number pattern

for i in range(5, 0, -1):
    print(" ".join(str(j) for j in range(i, 0, -1)))
print()

# Exercise 8: Reverse list

list1 = [10, 20, 30, 40, 50]
for num in reversed(list1):
    print(num)
print()

# Exercise 9: Display numbers from -10 to -1

for i in range(-10, 0):
    print(i)
print()

# Exercise 10: Display message after loop

for i in range(5):
    print(i)
print("Done!")
print()

# Exercise 11: Prime numbers within a range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime Numbers Between 25 and 50:")
for i in range(25, 51):
    if is_prime(i):
        print(i)
print()

