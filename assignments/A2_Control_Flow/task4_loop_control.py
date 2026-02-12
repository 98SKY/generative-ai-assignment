
daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break

    if sale == 0:
        print("No sales today — skipping")
        continue

    total_sales += sale
    print("Added:", sale, "| Running Total:", total_sales)

print("\nFinal Total Sales:", total_sales)
