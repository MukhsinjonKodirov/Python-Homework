# Handling ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling ValueError
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# Handling FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# Handling TypeError
try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Both inputs must be numbers.")
    result = int(num1) + int(num2)
except TypeError as e:
    print("Error:", e)

# Handling PermissionError
try:
    with open("protected_file.txt", "w") as file:
        file.write("Test data")
except PermissionError:
    print("Error: Permission denied.")

# Handling IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")

# Handling KeyboardInterrupt
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nError: Input interrupted by user.")

# Handling ArithmeticError
try:
    result = 1 / float("inf")  # This won't raise an error in Python but can be simulated
except ArithmeticError:
    print("Error: Arithmetic operation failed.")

# Handling UnicodeDecodeError
try:
    with open("unicode_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Unicode decoding failed.")

# Handling AttributeError
try:
    num = 10
    num.append(5)  # int does not have append method
except AttributeError:
    print("Error: Attribute not found.")
