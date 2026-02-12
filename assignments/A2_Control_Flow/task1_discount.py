
order_amount = input("Enter order amount: ")

# check numeric input
if not order_amount.isdigit():
    print("Invalid input! Please enter a number.")
    exit()

order_amount = int(order_amount)

# discount logic
if order_amount >= 2000:
    discount = 15
elif order_amount >= 1500:
    discount = 10
elif order_amount >= 1000:
    discount = 7
else:
    discount = 0

discount_amount = order_amount * discount / 100
final_amount = order_amount - discount_amount

# optional tax 5%
tax = final_amount * 0.05
total = final_amount + tax

print("Discount:", discount, "%")
print("Subtotal after discount:", final_amount)
print("Tax (5%):", tax)
print("Final Total:", total)
