# Parent Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


# Child Class
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        # Calling parent class constructor
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        # Calling parent class method
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# Creating object of IssuedBook
book1 = IssuedBook("Python Basics", "Guido van Rossum", "Madan", "03-02-2026")

# Displaying all details
book1.display_issued_book_details()
