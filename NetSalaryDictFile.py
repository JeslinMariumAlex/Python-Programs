import pickle

bfile = open("empfile", "wb")
n = int(input("Enter the number of employees:"))
print("Enter records of Employees")
i = 1
edata = dict()
while i <= n:
    print("Record No:", i)
    ename = input("Employee name:")
    ebasic = int(input("Basic Salary:"))
    ns = int(input("Enter the no of Night shifts: "))
    hra = ebasic * .15
    pf = ebasic * .08
    da = ebasic * .05
    totsal = ebasic + hra + da - pf + (ns * 300)
    print("NET SALARY:", totsal)
    edata["Empno"] = i
    edata["Name"] = ename
    edata["Basicsalary"] = ebasic
    edata["Totalsalary"] = totsal
    pickle.dump(edata, bfile)
    i = i + 1
bfile.close()
print("Reading the employee records from the file")
empno = 1
bfile = open("empfile", "rb")
while empno < n + 1:
    edata = pickle.load(bfile)
    print("Record Number:", empno)
    print(edata)
    empno = empno + 1
bfile.close()
