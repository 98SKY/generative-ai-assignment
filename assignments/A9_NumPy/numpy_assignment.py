import numpy as np

# Task 1: Creating NumPy Arrays

arr1 = np.arange(1, 11)
arr2 = np.arange(1, 10).reshape(3, 3)

arr3 = np.array([10, 20, 30, 40, 50])

print("1D Array:", arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("\n2D Array:\n", arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

print("\nArray from List:", arr3)
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)



# Task 2: Mathematical Operations

A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)
print("Power:", A ** 2)

# Optional NumPy functions
print("Using np.add:", np.add(A, B))
print("Using np.subtract:", np.subtract(A, B))



# Task 3: NumPy Mathematical Formulas

values = np.array([2, 4, 6, 8, 10])

print("Square Root:", np.sqrt(values))
print("Exponential:", np.exp(values))
print("Natural Log:", np.log(values))
print("Sum:", np.sum(values))
print("Cumulative Sum:", np.cumsum(values))



# Task 4: Aggregation Operations

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row-wise Sum:", np.sum(data, axis=1))
print("Column-wise Sum:", np.sum(data, axis=0))
print("Minimum Value:", np.min(data))
print("Maximum Value:", np.max(data))
print("Overall Mean:", np.mean(data))



# Task 5: Statistical Operations

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

range_marks = np.max(marks) - np.min(marks)
print("Range:", range_marks)



# Task 6: Percentiles & Sorting

sorted_marks = np.sort(marks)

print("Sorted Marks:", sorted_marks)
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))

average_marks = np.mean(marks)

above_average = np.sum(marks > average_marks)

print("Students Above Average:", above_average)



# Task 7: Sales Analysis

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

print("Total Weekly Sales:", np.sum(sales))
print("Average Daily Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))
print("Sales Standard Deviation:", np.std(sales))

avg_sales = np.mean(sales)

above_avg_days = sales[sales > avg_sales]

print("Days with Sales Above Average:", above_avg_days)