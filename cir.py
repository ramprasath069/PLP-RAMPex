class circle_area:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
n=int(input("Enter value: "))
c1=circle_area(n)
print(c1.area())
    