
# list named products containing at least 6 product names
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Speaker"]

# tuple sample_product (product_name, price, category)
sample_product = ("Laptop", 55000, "Electronics")

# Print the 2nd and last product
print("Second product:", products[1])
print("Last product:", products[-1])

# Append two new product names and print updated list
products.append("Webcam")
products.append("Microphone")

print("Updated product list:", products)

# Extra: Convert tuple → list → change price → back to tuple
temp = list(sample_product)
temp[1] = 52000  # new price
sample_product = tuple(temp)

print("Updated sample product:", sample_product)
