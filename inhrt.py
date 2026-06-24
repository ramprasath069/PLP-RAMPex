class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def deteils(self):
        print("The details: ")
        print(self.name)
        print(self.age)
class student(person):
    def student_details(self):
        print("The person is a student")

n=input("Enter name: ")
a=int(input("Enter age: "))
s1=student(n,a)
s1.student_details()
s1.deteils()