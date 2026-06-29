import csv

b = open("student.csv", "w", newline="")
writer = csv.writer(b)
writer.writerows([
    ["Name", "Age", "gender"],
    ["Karthikeyan", 25, "Male"],
    ["kavi", 30, "Male"],
    ["kamal", 28, "Male"]
])

b.close()

c = open("student.csv", "r")
data = csv.reader(c)

file1 = open("sample.txt", "w")

for i in data:
    print(i)
    file1.write(str(i) + "\n")   # Write each row into the text file

file1.close()
c.close()

f = open("sample.txt", "r")
print(f.read())
f.close()