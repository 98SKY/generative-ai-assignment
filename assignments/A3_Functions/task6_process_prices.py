def process_prices(prices):
    discounted = list(map(lambda x: x * 0.9, prices))
    filtered = list(filter(lambda x: x > 300, discounted))
    return discounted, filtered

d, f = process_prices([100, 500, 900, 50, 750])

print("Discounted:", d)
print("Filtered (>300):", f)
