from abc import ABC, abstractmethod

# Task 1 and 2: Product Class


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price     # Private attribute
        self.category = category

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.__price}")
        print(f"Category: {self.category}")

    # apply discount
    def apply_discount(self, percent):
        return self.__price - (self.__price * percent / 100)

    # Task 6: Magic Method
    def __str__(self):
        return f"Product({self.name}, {self.__price}, {self.category})"

    # Task 6: Operator Overloading
    def __add__(self, other):
        return self.__price + other.__price



# Task 3: Inheritance


class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        super().get_info()
        print(f"Warranty: {self.warranty_years} years")



# Task 4: Polymorphism


class Laptop(Product):
    def get_info(self):
        print("Laptop Details:")
        super().get_info()


class Mobile(Product):
    def get_info(self):
        print("Mobile Details:")
        super().get_info()


# Task 5: Abstraction


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of {amount}")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")



# Task 7: Inventory System


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.get_price()
        return total

    def show_all_products(self):
        for p in self.products:
            print(p)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price, category):
        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"Store: {self.store_name}")
        print(f"Total Products: {len(self.inventory.products)}")
        print(f"Total Value: {self.inventory.get_total_value()}")



# ------------------------------
# Testing All Tasks


print("\n--- Task 1 & 2 ---")
p1 = Product("Mouse", 500, "Accessories")
p2 = Product("Keyboard", 800, "Accessories")

p1.get_info()
print("Discounted Price:", p1.apply_discount(10))

p1.set_price(600)
print("Updated Price:", p1.get_price())


print("\n--- Task 3 ---")
ep = ElectronicProduct("Laptop", 70000, "Electronics", 2)
ep.get_info()


print("\n--- Task 4 ---")
items = [
    Laptop("Gaming Laptop", 90000, "Electronics"),
    Mobile("iPhone", 80000, "Electronics")
]

for item in items:
    item.get_info()


print("\n--- Task 5 ---")
cc = CreditCardPayment()
upi = UPIPayment()

cc.process_payment(5000)
upi.process_payment(3000)


print("\n--- Task 6 ---")
print(p1)  # __str__
print("Combined Price:", p1 + p2)  # __add__


print("\n--- Task 7 ---")
store = Store("Tech Store")
store.add_new_product("Monitor", 15000, "Electronics")
store.add_new_product("Headphones", 3000, "Accessories")
store.add_new_product("Webcam", 2500, "Accessories")

store.inventory.show_all_products()
store.show_summary()