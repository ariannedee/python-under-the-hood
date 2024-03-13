import copy


class Book:
    __lt__ = __le__ = __gt__ = __ge__ = None

    def __new__(cls, *args, **kwargs):
        print(f'__new__ called with {repr(cls)}, {repr(args)}, {repr(kwargs)}')
        obj = super().__new__(cls)
        return obj

    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f'__init__ called with {title}, {author}')

    def __del__(self):
        print(f"{self} destroyed")

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)})"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __bool__(self):
        """Returns True if no values are empty strings or None"""
        return bool(self.title) and bool(self.author)

    def __hash__(self):
        return hash((self.title, self.author))

    def __format__(self, format_spec):
        if not format_spec:
            return str(self)
        elif format_spec == 'u':
            return str(self).upper()
        elif format_spec == 't':
            return self.title
        elif format_spec == 'a':
            return self.author
        raise ValueError(f"Invalid format specifier {format_spec} for object of type 'Book'")


if __name__ == '__main__':
    book1 = Book('The Odyssey', 'Homer')  # __init__ called
    book2 = copy.copy(book1)
    print(str(book1))  # __str__ called
    print(book1)       # __str__ also called

    books = [book1, book2]
    print(repr(book1))  # __repr__ called
    print(books)        # __repr__ also called

    print(bool(book1))  # __bool__ called
    if book1:           # __bool__ also called
        print("Book 1 is True-ish")

    if book1 == book2:  # __eq__ called
        print("Same book")

    book2.title = 'The Iliad'
    if book1 != book2:  # __eq__ called even though __neq__ not implemented
        print("Different book")

    try:
        book1 > book2
    except TypeError as e:
        print(repr(e))

    num_reads = {
        book1: 1,
        book2: 2,
    }
    print(num_reads)  # book1 == book2 and hash(book1) == hash(book2) so only 1 entry made

    print(f"I LOVED {book1:u}")  # Calls __format__ with 'u'

    del book1
    print('Book 1 not destroyed yet because of reference in books')
