
with open("products.txt", "w") as file:
    for i in range(3):
        name = input("Enter product name: ")
        price = input("Enter price: ")
        file.write(name + " | " + price + "\n")

print("\nSaved Successfully!\n")

with open("products.txt", "r") as file:
    for line in file:
        print("Product ->", line.strip())
