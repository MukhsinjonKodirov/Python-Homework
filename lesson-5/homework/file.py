# 1. Leap Year Function
def is_leap(year):
   if not isinstance(year, int):
   raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 2. Conditional Statements Exercise
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# 3. Find Even Numbers Without Loop

# Solution 1: Using If-Else Statement
def find_even_numbers_if_else(a, b):
   
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b -= 1
    if a > b:
        return []
    return list(range(a, b + 1, 2))

# Solution 2: Without If-Else Statement
def find_even_numbers_no_if_else(a, b):
 
    return list(range(a + (a % 2), b + 1 - (b % 2), 2))
