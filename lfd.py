n=int(input())
star=1
a=n*2
for i in range(a):
    if(i<(a//2)-1):
        print(" "*n+"* "*star)
        star+=1
        n-=1
    else:
        print(" "*n+"* "*star)
        star-=1
        n+=1