class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = True

    def __str__(self):
        return f"{self.title} by {self.author} is {self.status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        borrowed_book_titles = ", ".join([book.title for book in self.borrowed_books])
        return f"Member: {self.name} (ID: {self.member_id}):\nBorrowed Books: {borrowed_book_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def lend_book(self, member, book):
        if book.status:
            book.status = False
            member.borrowed_books.append(book)
            print(f"{member.name} has borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available")

    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.status = True
            member.borrowed_books.remove(book)
            print(f"{member.name} has returned {book.title}")
        else:
            print(f"{member.name} did not borrow {book.title}")


# Example usage
book1 = Book("Entangled Life", "Merlin Sheldrake")
book2 = Book("The Three-Body Problem", "Liu Cixin")

# members
member1 = Member("Otis", 1001)
member2 = Member("Maeve", 1002)

# Library
library = Library()
library.add_book(book1)
library.add_book(book2)

# register members
library.add_member(member1)
library.add_member(member2)

# test lending and returns
library.lend_book(member1, book1)
library.lend_book(member2, book2)

# library.return_book(member1, book1)
# library.return_book(member1, book2)

print(member1)
print(member2)
