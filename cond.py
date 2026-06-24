def sample(n):
    if(n%3==0 and n%8==0):
        return f'{n} divisible by 3 and 8'
    else:
        return f'{n} not divisible by 3 and 8'
num=int(input("Enter a number: "))
print(sample(num))