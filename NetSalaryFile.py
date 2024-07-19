import pickle
bfile = open("empfile", "wb")
n = int(input("Enter the number of employees:"))
print("Enter records of Employees")
i = 1
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
    edata = [i, ename, ebasic, totsal]
    pickle.dump(edata, bfile)
    i=i+1
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
