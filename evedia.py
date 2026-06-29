n=int(input())
a=n*2
star=1
for i in range(a):
    if i<(a//2)-1:
        print(" "*n+"*"*star)
        star+=2
        n-=1
    else:
        print(" "*n+"*"*star)
        star-=2
        n+=1