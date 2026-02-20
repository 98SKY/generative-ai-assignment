sales = [1200, 450, 980, 1500, 3000]

# write to file
with open("sales_data.txt", "w") as file:
    for amount in sales:
        file.write(str(amount) + "\n")

print("Data written successfully!\n")

# reopen and read
with open("sales_data.txt", "r") as file:
    print("File Content:")
    print(file.read())
