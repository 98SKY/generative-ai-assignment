import matplotlib.pyplot as plt
import numpy as np

# --- Task 1: Line Plot (Sales Trend) ---
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1500, 1100, 1800, 2100, 1900]

plt.figure()
plt.plot(months, sales)
plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.show()

# --- Task 2: Scatter Plot (Relationship) ---
height = [150, 160, 165, 170, 175, 180]
weight = [50, 58, 62, 68, 75, 82]

plt.figure()
plt.scatter(height, weight)
plt.title('Height vs Weight Relationship')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

# --- Task 3: Bar Plot (Vertical & Horizontal) ---
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

# Vertical
plt.figure()
plt.bar(categories, values)
plt.title('Vertical Bar Chart')
plt.show()

# Horizontal
plt.figure()
plt.barh(categories, values)
plt.title('Horizontal Bar Chart')
plt.show()

# --- Task 4: Multiple Bar Plot (Yearly Comparison) ---
years = ['Product A', 'Product B', 'Product C']
sales_2022 = [400, 550, 300]
sales_2023 = [450, 600, 350]

x = np.arange(len(years))
width = 0.35

plt.figure()
plt.bar(x - width/2, sales_2022, width, label='2022')
plt.bar(x + width/2, sales_2023, width, label='2023')
plt.xticks(x, years)
plt.legend()
plt.title('Sales Comparison by Year')
plt.show()

# --- Task 5: Stacked Bar Chart ---
labels = ['Q1', 'Q2', 'Q3', 'Q4']
dept1 = [20, 35, 30, 35]
dept2 = [25, 32, 34, 20]

plt.figure()
plt.bar(labels, dept1, label='Dept 1')
plt.bar(labels, dept2, bottom=dept1, label='Dept 2')
plt.legend()
plt.title('Stacked Quarterly Performance')
plt.show()

# --- Task 6: Histogram (Marks Distribution) ---
marks = [55, 62, 65, 70, 72, 75, 78, 82, 85, 88, 90, 92, 95]

plt.figure()
plt.hist(marks, bins=5, edgecolor='black')
plt.title('Marks Distribution')
plt.xlabel('Marks Range')
plt.ylabel('Frequency')
plt.show()

# --- Task 7: Pie Chart (Market Share) ---
market_labels = ['Apple', 'Samsung', 'Google', 'Others']
shares = [35, 30, 15, 20]

plt.figure()
plt.pie(shares, labels=market_labels, autopct='%1.1f%%')
plt.title('Smartphone Market Share')
plt.show()
