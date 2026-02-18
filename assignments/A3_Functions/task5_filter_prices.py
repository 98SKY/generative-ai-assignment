prices = [100, 250, 400, 1200, 50, 2000, 850]

above_500 = list(filter(lambda x: x > 500, prices))
below_500 = list(filter(lambda x: x <= 500, prices))

print("Above 500:", above_500)
print("Below or equal 500:", below_500)
