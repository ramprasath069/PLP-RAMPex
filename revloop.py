n=int(input())
rev=0
while n>0:
    o=n%10
    rev=(rev*10)+o
    n=n//10
print(rev)
   