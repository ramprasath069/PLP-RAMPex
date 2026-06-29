n=int(input())
a=n*2
space=0
for i in range(a-1):
    if (i<(a//2)-1):
        print(" "*n)
        if i==0:
            print("*")
        else:
            print("*"+" "*(2*space-1)+"*")
        n-=1
        space+=1
    else:
        print(" "*n)
        if i==a-2:
            print("*")
        else:
            print("*"+" "*(2*space-1)+"*")
        n+=1
        space-=1