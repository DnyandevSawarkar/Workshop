import tkinter as tk
from tkinter import messagebox
import pandas as pd

class MarksheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Marksheet Fetcher")
        self.root.geometry("200x250")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Enter Roll Number:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Fetch Marksheet", command=self.fetch_marksheet)
        self.button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Bind the <Return> event to the fetch_marksheet function
        self.entry.bind("<Return>", self.fetch_marksheet)

    def fetch_marksheet(self, event=None):
        roll_number = self.entry.get()
        try:
            roll_number = int(roll_number)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid roll number.")
            return

        # Read the marksheet.csv file into a DataFrame
        try:
            df = pd.read_csv("marksheet.csv")
        except FileNotFoundError:
            messagebox.showerror("Error", "marksheet.csv file not found.")
            return

        # Filter the DataFrame based on the provided roll number
        result = df[df['Roll No.'] == roll_number]

        # If no match found for the roll number, show error message and clear previous result
        if result.empty:
            self.clear_result()
            messagebox.showerror("Error", "No record found for the provided roll number.")
            return

        # Extract the relevant information from the DataFrame
        name = result['Name'].values[0]
        math_marks = result['Maths'].values[0]
        physics_marks = result['Physics'].values[0]
        chemistry_marks = result['Chemistry'].values[0]

        # Calculate additional information
        total_marks_obtained = math_marks + physics_marks + chemistry_marks
        total_max_marks = 300  # Corrected total maximum marks
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

        # Display the marksheet details in the result label
        self.result_label.config(text=f"Roll Number: {roll_number}\n"
                                       f"Name: {name}\n"
                                       f"Mathematics: {math_marks}\n"
                                       f"Physics: {physics_marks}\n"
                                       f"Chemistry: {chemistry_marks}\n"
                                       f"Average: {average_marks:.2f}\n"
                                       f"Total marks obtained: {total_marks_obtained}\n"
                                       f"Total Maximum Marks: {total_max_marks}\n"
                                       f"Percentage: {percentage:.2f}%\n"
                                       f"Grade: {grade}\n"
                                       f"Remark: {remark}")

        # Clear the input after processing
        self.entry.delete(0, tk.END)

    def clear_result(self):
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarksheetApp(root)
    root.mainloop()
