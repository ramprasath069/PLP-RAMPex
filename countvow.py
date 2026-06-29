b=open("sample.txt","r")
content=b.read()
vowels=['a','e','i','o','u']
count=0
for i in content:
    if i in vowels:
        count+=1
print("The content of the file is:",content)
print("The number of vowels in the file is:",count)