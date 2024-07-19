class product:
    def __init__(self,name,count_a,count_b,count_c,):
        self.name=name
        self.count_a=count_a
        self.count_b=count_b
        self.count_c=count_c
        self.quantity
    def get_price(self):
        discount=0
        if self.count_a or self.count_b or self.count_c >10:
            discount=5
        elif self.total_quantity>20:
            discount=10
        print("Discount:",discount)
        Price of Product A:Rs.20
        Price of Product B:Rs.40
        Price of Product C:Rs.50
        print("Price of Product A:",Price of Product A)
        print("Price of Product B:",Price of Product B)
        print("Price of Product C:"Price of Product C)





name=input("Name of the customer:")
count_a=int(input("Count of Product A:"))
count_b=int(input("Count of Product B:"))
count_c=int(input("Count of Product C:"))
total_quantity=int(input("Enter total number of items:"))
p=price(name,count_a,count_b,count_c)


