# Task 3: Product Pricing (Dictionaries)

# 1. Create dictionary
price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000,
    "Speaker": 3000
}

# Add new product
price_dict["Webcam"] = 2500
print("After adding Webcam:", price_dict)

# Update price
price_dict["Mouse"] = 600
print("Updated Mouse price:", price_dict["Mouse"])

# Remove product safely
product_to_remove = "Tablet"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print("Product not found:", product_to_remove)

# Average price
total = sum(price_dict.values())
average = total / len(price_dict)
print("Average price:", average)

# Extra: max and min price product
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive:", max_product, price_dict[max_product])
print("Cheapest:", min_product, price_dict[min_product])
