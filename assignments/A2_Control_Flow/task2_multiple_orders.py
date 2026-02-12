
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Amount -> Discount% -> Final Amount")
print("------------")

for order in orders:

    if order >= 2000:
        discount = 15
    elif order >= 1500:
        discount = 10
    elif order >= 1000:
        discount = 7
    else:
        discount = 0

    discount_amount = order * discount / 100
    final_amount = order - discount_amount

    if discount > 0:
        discounted_orders += 1

    total_revenue += final_amount

    print(order, "->", discount, "% ->", final_amount)

print("\nTotal Revenue:", total_revenue)
print("Orders with discount:", discounted_orders)
