# task5_safe_shopping_cart.py

cart = []

while True:
    user_input = input("Enter price (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    except ValueError as e:
        print("Error:", e)

print("Total items:", len(cart))
print("Total bill:", sum(cart))
