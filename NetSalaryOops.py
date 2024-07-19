class employee:
    def __init__(self, name, code, bs):
        self.name = name
        self.code = code
        self.basic_sal = bs

    def calculate(self):
        self.da = self.basic_sal * (2 / 100)
        self.hra = self.basic_sal * (3 / 100)
        self.pf = self.basic_sal * (4 / 100)
        self.net = self.basic_sal + self.da + self.hra - self.pf

    def display(self):
        print("Name:", self.name)
        print("Code:", self.code)
        print("Basic Pay:", self.basic_sal)
        print("Net Salary:", self.net)


name = input("Name:")
code = input("Code:")
bp = int(input("BS:"))
e = employee(name, code, bp)
name1 = input("Name:")
code1 = input("Code:")
bp1 = int(input("BS:"))
e1 = employee(name1, code1, bp1)
e.calculate()
e.display
e1.calculate()
e1.display
