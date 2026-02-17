def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("5! =", factorial(5))
print("0! =", factorial(0))
print("-3! =", factorial(-3))
