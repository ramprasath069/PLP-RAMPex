def palindrome(s):
    b=s
    rev=0
    while s>0:
        rem=s%10
        rev=rev*10+rem
        s=s//10
    if rev==b:
        return "palindrome"
    else:
        return "not a palindrome"
num=int(input("Enter a number: "))
print(palindrome(num))