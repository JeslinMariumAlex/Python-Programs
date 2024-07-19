class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        self.ar=3.14*self.r*self.r
    def perimeter(self):
        self.per=2*3.14*self.r
    def display(self):
        print(self.ar)
        print(self.per)


s=Circle(3)
s.area()
s.perimeter()
s1=Circle(4)
s1.area()
s1.perimeter()
s.display()
s1.display()
