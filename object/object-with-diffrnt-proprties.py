#------------------------------Objects with Different Properties---------------------------

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

print(book1.get_info())  # Output: The Great Gatsby by F. Scott Fitzgerald, 180 pages
print(book2.get_info())  # Output: To Kill a Mockingbird by Harper Lee, 281 pages
