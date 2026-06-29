n=int(input())
space=1
for i in range(1,n+1):
    
    if i==1:
        print(" "*(n-1)+"*")
    elif(i<n):
        print(" "*(n-i-1)+"*"+" "*(2*space-1)+"*")
    else:
        print(" "*(n-i)+"*"*((i*2)-1))
    space+=1