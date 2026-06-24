class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("The area of rectangle is:",self.length*self.width)
l=int(input("Enter length: "))
w=int(input("Enter width: "))
r1=Rectangle(l,w)
r1.area()