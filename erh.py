try:
    a=int(input("Enter a number:"))
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Please enter a valid number")