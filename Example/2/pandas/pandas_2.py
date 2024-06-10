import pandas as pd

# Read a CSV file into a DataFrame
file_path = './example.csv'  # replace with your file path
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Get basic information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Get basic statistics of the DataFrame
print("\nDataFrame Statistics:")
print(df.describe())

# Select a specific column
column = df['salary']  
print("\nSelected Column (Salary):")
print(column)

# Filter rows based on a condition
filtered_df = df[df['age'] > 30] 
print("\nFiltered DataFrame (age > 30):")
print(filtered_df)

# Create a new column based on existing columns
df['salary_increase'] = df['salary'] * 1.1  
print("\nDataFrame with New Column (Salary Increase):")
print(df.head())

# Group by a column and calculate aggregate statistics
grouped_df = df.groupby('department').agg({'salary': 'mean'}) 
print("\nGrouped DataFrame (mean salary):")
print(grouped_df)


# Handle missing values
df_filled = df.fillna(0)  
print("\nDataFrame with Filled NaN Values:")
print(df_filled.head())

# Save the processed DataFrame to a new CSV file
df.to_csv('processed_example.csv', index=False)
