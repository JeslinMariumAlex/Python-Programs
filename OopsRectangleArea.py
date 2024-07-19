class Rectangle:
    def __init__(self, l, b):
        self.ar = None
        self.per = None
        self.len = l
        self.bre = b

    def area(self):
        self.ar = self.len * self.bre

    def perimeter(self):
        self.per = 2 * (self.len + self.bre)

    def display(self):
        print("Area:", self.ar)
        print("Perimeter:", self.per)


s = Rectangle(4, 5)
s.area()
s.perimeter()
s1 = Rectangle(6, 3)
s1.area()
s1.perimeter()
s.display()
s1.display()
