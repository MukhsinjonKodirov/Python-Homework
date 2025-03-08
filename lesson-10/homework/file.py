# Homework 1: ToDo List Application

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {self.description} (Due: {self.due_date}) [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return f"Task '{title}' marked as complete."
        return "Task not found."
    
    def list_tasks(self):
        return [str(task) for task in self.tasks]
    
    def list_incomplete_tasks(self):
        return [str(task) for task in self.tasks if not task.completed]

# Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)
    
    def list_posts(self):
        return [str(post) for post in self.posts]
    
    def posts_by_author(self, author):
        return [str(post) for post in self.posts if post.author == author]
    
    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]
    
    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                return "Post updated."
        return "Post not found."

# Homework 3: Simple Banking System

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrawn {amount}. Remaining balance: {self.balance}"
    
    def transfer(self, recipient, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.withdraw(amount)
        recipient.deposit(amount)
        return "Transfer successful."
    
    def __str__(self):
        return f"Account {self.account_number} - {self.holder_name}: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        self.accounts[account.account_number] = account
    
    def check_balance(self, account_number):
        return self.accounts.get(account_number, "Account not found.")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            return "Deposit successful."
        return "Account not found."
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return "Account not found."
    
    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            return self.accounts[from_acc].transfer(self.accounts[to_acc], amount)
        return "One or both accounts not found."

