
# Parallel list of categories
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Speaker"]
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Audio"]

# 1. Create set of categories
categories_set = set(categories)
print("Unique categories:", categories_set)

# 2. Add new category and show duplicates ignored
categories_set.add("Gaming")
categories_set.add("Audio")  # duplicate

print("After adding categories:", categories_set)

# 3. Check if category exists
print("Is 'Electronics' present?", "Electronics" in categories_set)

# Extra: total number of unique categories
print("Total unique categories:", len(categories_set))
