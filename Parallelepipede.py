class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Length of the Rectangle:", self.length)
        print("Width of the Rectangle:", self.width)
        print("Perimeter of the Rectangle:", self.perimeter())
        print("Area of the Rectangle:", self.area())


class Parallelepipede(Rectangle):
    def __init__(self, l, w, h):
        Rectangle.__init__(self, l, w)
        self.height = h

    def volume(self):
        return self.length * self.width * self.height

    def surfaceArea(self):
        return 2 * (self.length * self.width) + 2 * (self.width * self.height) + 2 * (self.length * self.height)

    def display(self):
        print("Length of the Parallelepipede:", self.length)
        print("Width of the Parallelepipede", self.width)
        print("Height of the Parallelepipede", self.height)
        print("Perimeter of the Rectangle:", self.perimeter())
        print("Area of the Rectangle:", self.area())
        print("Volume of the Parallelepipede:", self.volume())
        print("Surfacearea of the Parallelepipede:", self.surfaceArea())


l = int(input("Enter the length of the Rectangle:"))
w = int(input("Enter the width of the Rectangle:"))
h = int(input("Enter the height of the Rectangle:"))
print("\n\t\tResult")
print("____________________________")
pp = Parallelepipede(l, w, h)
pp.display()
