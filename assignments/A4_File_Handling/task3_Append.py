
new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
    for amount in new_sales:
        file.write(str(amount) + "\n")

print("New data appended!\n")

# show updated file
with open("sales_data.txt", "r") as file:
    content = file.readlines()
    print("Updated File:")
    print("".join(content))
    print("Total lines:", len(content))
