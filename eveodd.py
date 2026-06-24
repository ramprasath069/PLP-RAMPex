def EvenOdd(a):
    if(a%2==0):
        return "Even"
    else:
        return "Odd"
b=EvenOdd(3)
print(b)


#--------------lambda------

b=lambda a:print("even") if a%2==0 else print("odd")
print(b)