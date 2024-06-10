import pandas as pd

# Read student data from CSV file
file_path = 'students.csv'
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
column = df['Grade']
print("\nSelected Column (Grade):")
print(column)

# Filter rows based on a condition
filtered_df = df[df['Age'] > 20]
print("\nFiltered DataFrame (Age > 20):")
print(filtered_df)

# Create a new column based on existing columns
df['Total Marks'] = df['Maths'] + df['Physics'] + df['Chemistry']
print("\nDataFrame with New Column (Total Marks):")
print(df.head())

# Group by a column and calculate aggregate statistics
grouped_df = df.groupby('Gender').agg({'Maths': 'mean', 'Physics': 'mean', 'Chemistry': 'mean'})
print("\nGrouped DataFrame (mean by Gender):")
print(grouped_df)


# Handle missing values
df_filled = df.fillna(0)
print("\nDataFrame with Filled NaN Values:")
print(df_filled.head())

# Save the processed DataFrame to a new CSV file
df.to_csv('processed_students.csv', index=False)
