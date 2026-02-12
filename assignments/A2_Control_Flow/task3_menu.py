
orders = []

while True:
    print("\n1 - Add Order")
    print("2 - Show Orders")
    print("q - Quit")

    choice = input("Enter choice: ")

    if choice == '1':
        amount = input("Enter order amount: ")

        if not amount.isdigit():
            print("Invalid input!")
            continue

        orders.append(int(amount))
        print("Order added!")

    elif choice == '2':

        if len(orders) == 0:
            print("No orders yet")
            continue

        print("\nOrder Summary")
        for order in orders:

            if order >= 2000:
                discount = 15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            else:
                discount = 0

            final = order - (order * discount / 100)
            print(order, "->", discount, "% ->", final)

    elif choice == 'q':
        print("Exiting program...")
        break

    else:
        print("Invalid option! Try again.")
