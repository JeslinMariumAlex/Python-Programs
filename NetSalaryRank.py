class employee:
    def __init__(self, name, code, bs):
        self.name = name
        self.code = code
        self.bs = bs

    def calculate(self):
        self.da = self.bs * (2 / 100)
        self.hra = self.bs * (3 / 100)
        self.pf = self.bs * (4 / 100)
        self.net = self.bs + self.da + self.hra - self.pf

    def display(self):
        print("Employee Record")
        print("_______________")
        print("Name:", self.name)
        print("Code:", self.code)
        print("Basic Pay:", self.bs)
        print("Net Salary:", self.net)


emp = []
n = int(input("Enter the number of employees:"))
for i in range(0, n):
    name = input("Name:")
    code = input("Code:")
    bp = int(input("BS:"))
    e = employee(name, code, bp)
    e.calculate()
    emp.append(e)
for s1 in emp:
    s1.display()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if emp[i].net < emp[j].net:
            x = emp[i]
            emp[i] = emp[j]
            emp[j] = x
print("\n\nRank\tName\tCode\tNet Salary")
for i in range(0, n):
    print(i + 1, "\t\t", emp[i].name, "\t\t", emp[i].code, "\t\t", emp[i].net)
