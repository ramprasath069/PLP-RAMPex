class NagativeNumError(Exception):
    pass
try:
    num=int(input("Enter a num: "))
    if num<0:
        raise NagativeNumError("Negative number is not allowed")
    else:
        print("The number is : ",num)
except NagativeNumError as e:
    print(e)