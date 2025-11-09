class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other) -> bool:
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 250)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book4 = Book("1984", "George Orwell", 328)
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book6 = Book("Pride and Prejudice", "Jane Austen", 279)
book7 = Book("Pride and Prejudice", "Jane Austen", 390)

books = [book1, book2, book3, book4, book5, book6]

for book in books:
    print(book)

print(book6 == book7)
print(book4 > book2)
print(book1 < book7)
print(book2 + book3)

print("Mockingbird" in book3)  # TypeError: argument of type 'Book' is not iterable
print("Mockingbird" in book1)

for book in books:
    print(book["title"])
    print(book["author"])
    print(book["num_pages"])
    print(book["audio"])
