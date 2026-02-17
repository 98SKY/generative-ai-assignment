def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)

prices_list = []

while True:
    print("\n1 Add Price")
    print("2 Show Average")
    print("3 Show Highest")
    print("q Quit")

    choice = input("Enter choice: ")

    if choice == '1':
        price = float(input("Enter price: "))
        add_price(prices_list, price)

    elif choice == '2':
        print("Average Price:", get_average_price(prices_list))

    elif choice == '3':
        print("Highest Price:", get_max_price(prices_list))

    elif choice == 'q':
        break

    else:
        print("Invalid choice")
