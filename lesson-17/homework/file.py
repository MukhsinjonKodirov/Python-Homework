import pandas as pd
import numpy as np

# Homework 1
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

df.rename(columns={"First Name": "first_name", "Age": "age"}, inplace=True)
print(df.head(3))
mean_age = df["age"].mean()
print(mean_age)
print(df[["first_name", "City"]])
df["Salary"] = np.random.randint(30000, 80000, df.shape[0])
print(df.describe())

# Homework 2
sales_and_expenses = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
})

print(sales_and_expenses["Sales"].max(), sales_and_expenses["Expenses"].max())
print(sales_and_expenses["Sales"].min(), sales_and_expenses["Expenses"].min())
print(sales_and_expenses["Sales"].mean(), sales_and_expenses["Expenses"].mean())

# Homework 3
expenses = pd.DataFrame({
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
})

expenses.set_index("Category", inplace=True)
print(expenses.max(axis=1))
print(expenses.min(axis=1))
print(expenses.mean(axis=1))

