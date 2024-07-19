class student:
    def __init__(self, name, rollno, p, c, m):
        self.total = None
        self.avg = None
        self.name = name
        self.rollno = rollno
        self.p = p
        self.c = c
        self.m = m

    def calculate(self):
        self.total = self.p + self.c + self.m
        self.avg = (self.total / 300) * 100
        if self.per >= 90:
            print("Grade is A")
        elif self.per >= 80:
            print("Grade is B")
        elif self.per >= 70:
            print("Grade is C")
        elif self.per >= 60:
            print("Grade is D")
        elif self.per >= 50:
            print("Grade is E")
        else:
            print("Grade is F")

student_list=[]
n=int(input("Enter the number of students"))
for i in range(0,n):
    name = input("Enter the name: ")
    rollno = int(input("Enter the Rollno:"))
    p = int(input("Physics:"))
    c = int(input("Chemistry:"))
    m = int(input("Maths:"))
    s = student(name, rollno, p, c, m)
    s.calculate()
    student_list.append(s)
