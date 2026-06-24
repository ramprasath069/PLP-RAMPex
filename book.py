l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print(l1+l2)class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
book_name=input("Enter book name: ")
author_name=input("Enter author name: ")
b1=book(book_name,author_name)
b1.display()