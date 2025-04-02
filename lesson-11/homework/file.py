# Task 1

python -m venv myenv
myenv\Scripts\activate
pip install numpy requests

# Task 2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Task 3
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)





