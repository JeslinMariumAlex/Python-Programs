class student:
    def __init__(self,name,per):
        self.name=name
        self.pe=per
    def display(self):
        print("Name is:",self.name)
        if(self.pe>=90):
            print("Grade is A")
        elif (self.pe >= 80):
            print("Grade is B")
        elif (self.pe >= 70):
            print("Grade is C")
        elif (self.pe >= 60):
            print("Grade is D")
        elif (self.pe >= 50):
            print("Grade is E")
        else :
            print("Grade is F")
name=input("Name:")
p=int(input("Physics:"))
c=int(input("Chemistry:"))
m=int(input("Maths:"))
per=((p+c+m)/300)*100
s=student(name,per)
name1=input("Name:")
p1=int(input("Physics:"))
c1=int(input("Chemistry:"))
m1=int(input("Maths:"))
per1=((p+c+m)/300)*100
s1=student(name1,per1)
s.display()
s1.display()


