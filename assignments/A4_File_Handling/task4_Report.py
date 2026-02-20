
numbers = []

with open("sales_data.txt", "r") as file:
    for line in file:
        numbers.append(int(line.strip()))

total = sum(numbers)
highest = max(numbers)
lowest = min(numbers)
average = total / len(numbers)

print("Total Sales:", total)
print("Highest Sale:", highest)
print("Lowest Sale:", lowest)
print("Average Sale:", average)
