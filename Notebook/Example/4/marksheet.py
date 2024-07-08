import pandas as pd

def fetch_marksheet(roll_number):
    # Read the marksheet.csv file into a DataFrame
    df = pd.read_csv("./marksheet.csv")

    # Filter the DataFrame based on the provided roll number
    result = df[df['Roll No.'] == roll_number]

    # If no match found for the roll number, return None
    if result.empty:
        print("No record found for the provided roll number.")
        return None
    
    # Extract the relevant information from the DataFrame
    name = result['Name'].values[0]
    math_marks = result['Maths'].values[0]
    physics_marks = result['Physics'].values[0]
    chemistry_marks = result['Chemistry'].values[0]

    # Calculate additional information
    total_marks_obtained = math_marks + physics_marks + chemistry_marks
    total_max_marks = 300
    average_marks = total_marks_obtained / 3
    percentage = (total_marks_obtained / total_max_marks) * 100

    # Define the grade based on percentage
    if percentage >= 90:
        grade = 'A'
    elif 80 <= percentage < 90:
        grade = 'B'
    elif 70 <= percentage < 80:
        grade = 'C'
    elif 60 <= percentage < 70:
        grade = 'D'
    else:
        grade = 'F'

    # Define the remark based on grade
    if grade == 'A':
        remark = 'Excellent'
    elif grade == 'B':
        remark = 'Very Good'
    elif grade == 'C':
        remark = 'Good'
    elif grade == 'D':
        remark = 'Average'
    else:
        remark = 'Fail'

    # Print the marksheet
    print("Roll Number:", roll_number)
    print("Name:", name)
    print("Mathematics:", math_marks)
    print("Physics:", physics_marks)
    print("Chemistry:", chemistry_marks)
    print("Average:", average_marks)
    print("Total marks obtained:", total_marks_obtained)
    print("Total Maximum Marks:", total_max_marks)
    print("Percentage:", "{:.2f}".format(percentage), "%")
    print("Grade:", grade)
    print("Remark:", remark)

# Example usage
if __name__ == "__main__":
    while(1):
        roll_number = input("Enter Roll Number: ")
        fetch_marksheet(int(roll_number))
