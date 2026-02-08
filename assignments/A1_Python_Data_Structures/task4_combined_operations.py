# Task 4: Combined Operations

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Speaker"]
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Audio"]

price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000,
    "Speaker": 3000
}

# 1. Create catalog list of tuples (product, price, category)
catalog = []
for i in range(len(products)):
    name = products[i]
    catalog.append((name, price_dict[name], categories[i]))

print("Catalog:", catalog)

# 2. Create category_to_products dictionary
category_to_products = {}

for item in catalog:
    product, price, category = item
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("Category mapping:", category_to_products)

# 3. Print products in category having maximum products
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))
print("Category with most products:", max_category)
print("Products in that category:", category_to_products[max_category])