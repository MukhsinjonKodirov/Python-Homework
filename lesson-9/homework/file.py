# 1. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# 2. Person Class
from datetime import date
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date
    
    def age(self):
        today = date.today()
        birth_year = int(self.birth_date.split('-')[0])
        return today.year - birth_year

# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"

# 4. Shape and Subclasses
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# 5. Binary Search Tree Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None or node.value == value:
            return node is not None
        return self._search(node.left, value) if value < node.value else self._search(node.right, value)

# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

# 7. Linked List Data Structure
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=' -> ')
            temp = temp.next
        print("None")

# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, item, price):
        self.items[item] = price
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    def total_price(self):
        return sum(self.items.values())

# 9. Stack with Display
class StackWithDisplay(Stack):
    def display(self):
        print(self.stack if self.stack else "Stack is empty")

# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue is empty"

# 11. Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, name, balance):
        self.accounts[name] = balance
    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
    def check_balance(self, name):
        return self.accounts.get(name, "Account not found")
