import pandas as pd

# Sample data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Black', 'Emily White', 'Daniel Green', 'Laura Blue', 'Peter Red', 'Anne Purple'],
    'age': [28, 34, 45, 29, 25, 32, 40, 38, 50, 27],
    'salary': [50000, 60000, 70000, 55000, 48000, 62000, 58000, 63000, 72000, 51000],
    'department': ['HR', 'Engineering', 'Sales', 'Engineering', 'HR', 'Marketing', 'Sales', 'Engineering', 'Marketing', 'HR']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('example.csv', index=False)

print("CSV file created successfully!")
