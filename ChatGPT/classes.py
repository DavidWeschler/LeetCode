"""You are tasked with designing a simple library system where users can borrow and return books."""

class Book:
    def __init__(self, tite: str, author: str, year_published: int, available: bool = True) -> None:
        self.__title = tite
        self.__author = author
        self.__yearPublished = year_published
        self.__available = available
    
    def __str__(self) -> str:
        return f"Book Tite: {self.__title}\nAuthor: {self.__author}\nYear: {self.__yearPublished}\nAvailable: {"yes" if self.__available else "no"}\n"

    def borrow(self):
        if self.__available:
            self.__available = False
    
    def return_book(self):
        self.__available = True


class User:
    def __init__(self, name: str, borrowed_books: list[Book] = []) -> None:
        self.__name = name
        self.__borrowed_books = borrowed_books

    def __str__(self) -> str:
        return f""
    
    def borrow_book(self, book: Book):
        book.borrow()
        self.__borrowed_books.append(book)
    
    def return_book(self, book: Book):
        book.return_book()
        self.__borrowed_books.remove(book)

# got = Book("GOT", "Tolkin", 1998, False)
# hp = Book("Harry Potter", "JK Rowling", 2001)
# print(got)
# print(hp)