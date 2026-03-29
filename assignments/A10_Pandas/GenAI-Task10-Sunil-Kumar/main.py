# Task 1: Pandas Series Basics
import pandas as pd
import matplotlib.pyplot as plt

# 2. Create Series
marks_list = [78, 85, 90, 66, 72]
marks = pd.Series(marks_list)

# 4. Print values, index, and data type
print("--- Task 1: Series Basics ---")
print("Series Values:\n", marks.values)
print("Index:", marks.index)
print("Data Type:", marks.dtype)

# 5. Access elements
print("First Element:", marks[0])
print("Last Two Elements:\n", marks.tail(2))

# ---
# Task 2: Mathematical Operations on Series
print("\n--- Task 2: Mathematical Operations ---")
print("Add 5 (Grace marks):\n", marks + 5)
print("Subtract 2:\n", marks - 2)
print("Multiply by 1.05:\n", marks * 1.05)
print("Divide by 2:\n", marks / 2)

# ---
# Task 3: Python Functionalities on Series
print("\n--- Task 3: Series Functionalities ---")
print("Max:", marks.max())
print("Min:", marks.min())
print("Sum:", marks.sum())
print("Mean:", marks.mean())

# Apply lambda for pass status (>= 70)
pass_status = marks.apply(lambda x: x >= 70)
print("Passed Status:\n", pass_status)
print("Count of students passed:", pass_status.sum())

# ---
# Task 4: Create a DataFrame
data = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
students = pd.DataFrame(data)

print("\n--- Task 4: DataFrame Creation ---")
print("First 3 rows:\n", students.head(3))
print("Last 2 rows:\n", students.tail(2))
print("Shape:", students.shape)
print("Columns:", students.columns.tolist())

# ---
# Task 5: Important DataFrame Functions
print("\n--- Task 5: DataFrame Functions ---")
students.info()
print("\nDescribe:\n", students.describe())

# Sorting and resetting index
students_sorted = students.sort_values(by='Marks', ascending=False).reset_index(drop=True)
print("\nSorted by Marks (Desc):\n", students_sorted)

# ---
# Task 6: Filtering & Conditional Selection
print("\n--- Task 6: Filtering ---")
print("Marks > 75:\n", students[students['Marks'] > 75])
print("Subject is Math:\n", students[students['Subject'] == 'Math'])
print("Above average marks:\n", students[students['Marks'] > students['Marks'].mean()])
print("Failed (< 70):\n", students[students['Marks'] < 70])

# ---
# Task 7: Grouping & Basic Analysis
print("\n--- Task 7: Grouping ---")
print("Avg marks per subject:\n", students.groupby('Subject')['Marks'].mean())
print("Student count per subject:\n", students.groupby('Subject')['Name'].count())
print("Max marks per subject:\n", students.groupby('Subject')['Marks'].max())

# ---
# Task 8: Pandas Plotting
# Note: These will display if using a Jupyter Notebook or IDE with plot support
students.plot(kind='bar', x='Name', y='Marks', title='Student Names vs Marks')
students['Marks'].plot(kind='line', title='Marks Trend')
students['Marks'].plot(kind='hist', title='Distribution of Marks')

# ---
# Task 9: Mini Use Case: Sales Data Analysis
sales_data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}
sales = pd.DataFrame(sales_data)

print("\n--- Task 9: Sales Analysis ---")
print("Total Revenue:", sales['Revenue'].sum())
avg_rev = sales['Revenue'].mean()
print("Average Daily Revenue:", avg_rev)
print("Day with Highest Revenue:\n", sales[sales['Revenue'] == sales['Revenue'].max()])
print("Days where Revenue > Average:\n", sales[sales['Revenue'] > avg_rev])

# Plotting Sales
sales.plot(kind='line', x='Day', y='Revenue', marker='o', title='Revenue vs Day')
plt.show()
