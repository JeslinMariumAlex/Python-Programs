import pickle
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


f = open("employeefile", "wb")
n1 = input("Enter the name of first employee:")
c1 = input("Enter the code of first employee:")
bs1 = int(input("Enter the Basic Salary of first employee:"))
emp1 = employee(n1, c1, bs1)
emp1.calculate()
pickle.dump(emp1, f)
print("displaying")
print("____________________")
print("____________________")
f.close()
print("Reading data from file")
print("____________________")
f = open("employeefile", "rb")
emp = pickle.load(f)
emp.display()
f.close()
