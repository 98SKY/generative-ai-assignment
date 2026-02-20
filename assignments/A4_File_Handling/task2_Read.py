# read()
with open("sales_data.txt", "r") as file:
    print(file.read())

# readline()
with open("sales_data.txt", "r") as file:
    print(file.readline())

# readlines()
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    numbers = []

    for line in lines:
        numbers.append(int(line.strip()))

    print(numbers)
