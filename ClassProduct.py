class product:
    def __init__(self, name, stock, quantity):
        self.name = name
        self.stock = stock
        self.quantity = quantity

    def get_price(self):
        if self.quantity < 10:
            pass
        elif 10 < self.quantity < 99:
            discount = 10
        else:
            discount = 20
        print("discount:", discount)
        price = (100 - discount) / 100 * self.price
        self.price = price * self.quantity
        return (self.price)

    def make_purchase(self):
        self.stock -= self.quantity
        print("Stock remaining=", self.stock)

    def display(self):
        print("Product Name:", self.name)
        print("Poduct quantity:", self.quantity)
        print("Product.price:", self.price)
        print("Product remaining:", self.stock)


name = input("Name:")
count = int(input("Count of items:"))
price = int(input("Price of items:"))
quantity = int(input("Amount of items to buy:"))
p = product(name, count, price, quantity)
print("Total amount:")
print(p.get_price)
print("Stock remaining")
p.make_purchase()
p.display()
