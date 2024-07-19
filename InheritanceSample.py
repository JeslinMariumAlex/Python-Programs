class employee:
    def __init__(self, ename, ecode, ebs):
        self.emp_name = ename
        self.emp_code = ecode
        self.emp_basic = ebs

    def calculate(self):
        if self.emp_basic<10000:
            self.emp_da = self.basic * (2 / 100)
            self.emp_hra = self.basic * (3 / 100)
            self.emp_pf = self.basic * (4 / 100)
        else:
            self.emp_da = self.basic * (2 / 100)
            self.emp_hra = self.basic * (3 / 100)
            self.emp_pf = self.basic * (4 / 100)
            self.emp_ns = self.basics + self.da + self.hra - self.pf
    def display(self):
        print("Name:", self.emp_name)
        print("EmpCode:", self.emp_code)
        print("Basic Salary:", self.emp_basic)
        print("DA:", self.emp_da)
        print("HRA:", self.emp_hra)
        print("PF:", self.emp_pf)
        print("Net Salary:", self.emp_pf)

class teacher(employee):
    def __init__(self,enm,ecd,ebs,dept):
        employee.__init__(self,enm,ecd,ebs)
        self.department=dept
        self.student=[]
    def mark_attendence(self,n):
        self.count=n
        print("Enter the attendance roollno wise(p-present/a-absent)")
        for i in range(0,n):
            att=input()
            self.student.append(att)
    def display_attendance(self):
        c=0
        print("Count of present students")
        for i in range(0,self.count):
            if self.student[i].low()=="p":
                c=c+1
        print(c)

    def display(self):
        print("Name:", self.emp_name)
        print("EmpCode:", self.emp_code)
        print("Department:", self.department)
        print("Basic Salary:", self.emp_basic)
        print("DA:", self.emp_da)
        print("HRA:", self.emp_hra)
        print("PF:", self.emp_pf)
        print("Net Salary:", self.emp_ns)
teacher_list=[]
m=int(input("Enter the number of teachers"))
for i in range(0,m):
    name=input("Enter the name of teachers")
    c = input("Enter the code of teachers")
    bs = int(input("Enter the basic salary of teachers"))
    dept = input("Enter the department of teachers")
    no = int(input("Enter the department of teachers"))
    tchr=teacher(name,c,bs,dept)
    tchr.mark_attendence(no)
    tchr.calculate()
    teacher_list.append(tchr)
for i in range(0,m):
    print("___________________________")
    teacher_list[i].display()
    teacher_list[i].display_attendance()


