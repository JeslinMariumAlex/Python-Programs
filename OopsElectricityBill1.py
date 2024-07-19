class ebill:
    def __init__(self, name, con_no, unit):
        self.amount = None
        self.name = name
        self.con_no = con_no
        self.unit = unit

    def calculate(self):
        if self.unit < 100:
            self.amount = self.unit * 0.5
        elif self.unit < 200:
            self.amount = (100 * 0.5) + (self.unit - 100) * 1.5
        elif self.unit < 500:
            self.amount = (100 * 0.5) + (100 * 2) + (self.unit - 200) * 3
        else:
            self.amount = (100 * 0.5) + (200 * 3.5) + (200 * 4.6) + (self.unit - 500) * 6.6

    def display(self):
        print("Electricity Bill")
        print("________________")
        print("Consumer Name:", self.name)
        print("Consumer Number:", self.con_no)
        print("Consumed Unit:", self.unit)
        print("Amount to be paid:", self.amount)


bill_list = []
n = int(input("Enter the number of Customers:"))
for i in range(0, n):
    name = input("Enter the Consumer name:")
    con_no = input("Enter the Consumer number:")
    u = int(input("Enter the Consumed Unit:"))
    e = ebill(name, con_no, u)
    e.calculate()
    bill_list.append(e)
for i in range(0, n):
    bill_list[i].display()
