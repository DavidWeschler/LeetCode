"""You are tasked with designing a simple library system where users can borrow and return books."""

class Book:
    def __init__(self, title: str, author: str, year_published: int, available: bool = True) -> None:
        self.__title = title
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
    
    @property
    def available(self):
        return self.__available


class User:
    def __init__(self, name: str, borrowed_books: list[Book] = None) -> None:
        self.__name = name
        if borrowed_books is None:
            borrowed_books = []
        self.__borrowed_books = borrowed_books

    def __str__(self) -> str:
        books = "".join(str(b)+'\n' for b in self.__borrowed_books)
        return f"Name: {self.__name}\nBooks:\n------------\n{books if books else "No borrowed books"}"
    
    def borrow_book(self, book: Book):
        book.borrow()
        self.__borrowed_books.append(book)
    
    def return_book(self, book: Book):
        book.return_book()
        self.__borrowed_books.remove(book)


class Library:
    def __init__(self, books: list[Book] = [], users: list[User] = []) -> None:
        self.__books = books
        self.__users = users
    
    def add_book(self, book: Book):
        self.__books.append(book)
    
    def add_user(self, user: User):
        self.__users.append(user)
    
    def lend_book(self, user: User, book: Book):
        if book.available:
            user.borrow_book(book)

    def receive_book(self, user: User, book: Book):
        user.return_book(book)
        book.return_book()
    
    def list_available_books(self):
        return [book for book in self.__books if book.available]


# Creating book instances
book1 = Book("GOT", "George R.R. Martin", 1996, False)
book2 = Book("Harry Potter", "J.K. Rowling", 2001)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book4 = Book("1984", "George Orwell", 1949)
book5 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)

# Creating a user instance
user1 = User("David Weschler")

# Displaying initial state of books and user
# print("Initial state of books:")
# print(book1)
# print(book2)
# print(book3)
# print(book4)
# print(book5)

# print("\nInitial state of user:")
# print(user1)

# User borrows some books
user1.borrow_book(book2)  # Borrowing Harry Potter
user1.borrow_book(book4)  # Borrowing 1984

# Displaying the state after borrowing
print(user1)
# print(book2)
# print(book4)

# # User returns a book
# user1.return_book(book2)  # Returning Harry Potter

# # Displaying the state after returning
# print("\nAfter returning Harry Potter:")
# print(user1)
# print(book2)
