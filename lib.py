class Library:
    def __init__(self):
        self.books = ["pyhton", "java"]

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)
    def borrow_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed {book}.")
        else:
            print(f"Sorry, {book} is not available in the library.")
    def return_book(self,book):
        self.books.append(book)
        print(f"You have returned {book}.")
book_name=input("Enter book name: ")
l1=Library()
l1.add_book(book_name)
l1.display_books()
l1.borrow_book(book_name)
l1.display_books()
l1.return_book(book_name)
l1.display_books()