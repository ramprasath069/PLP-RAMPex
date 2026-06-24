year = int(input())
if(year%4==0):
    print("leaf year")
elif(year%400==0):
    print("leaf year")
elif(year%100==0):
    print("not leaf year")
else:
    print("not leaf year")