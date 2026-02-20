prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

with open("discount_report.txt", "w") as file:
    total = 0
    count = 0

    for product in prices:
        original = prices[product]
        discounted = original - (original * discount / 100)

        file.write(f"{product} | {original} | {round(discounted,2)}\n")

        total += discounted
        count += 1

    avg = total / count
    file.write(f"\nTotal Items: {count}")
    file.write(f"\nAverage Discounted Price: {round(avg,2)}")

# display file
with open("discount_report.txt", "r") as file:
    print("\nReport:\n")
    print(file.read())
