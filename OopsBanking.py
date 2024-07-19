class bankaccount:
    def __init__(self, name, acc_no):
        self.balance=0
        self.name = name
        self.acc_no = acc_no

    def deposit(self):
        amount=float(input("Enter the amount to be deposited"))
        self.balance=self.balance=amount
        print("amount deposited",amount)

    def withdrawal(self):
        amount=float(input("enter amount to be withdrawn"))
        if self.balance>=amount
            self.balance=

    def display(self):
        print("name")
        print("account number")
        print("Available balance")



name = input("Enter the Customer name ")
acc_no = input("Enter the Account number")
s = bankaccount(acc_no, name)
print("Banking")
print("1.Display\n2.Deposit\n3.Withdraw\n4.Exit")
while(True):
    ch=int(input("Enter the choice"))
    if ch==1:
        s.display()
    elif ch==2:
        s.deposit()
    elif ch==3:
        s.withdrawal()
    elif ch==4:
        print("Exiting")
        break
    else:
        print("Invalid choice")
