class investment:
    def __init__(self,p,i):
        self.p=p
        self.i=i
    def valueafter(self):
        n=int(input("Enter the number of years:"))
        self.valueafter=self.p(1+(self.i/100))**n
    def display(self):
        print("value after n years:",self.valueafter)

p=int(input("Enter the principal amount:"))
i=int(input("Enter the interest rate:"))
invset=investment(p,i)
invest.valueafter()
invset.display()