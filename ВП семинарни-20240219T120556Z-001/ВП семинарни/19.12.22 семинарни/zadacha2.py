class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __str__(self):
        return f'((self.book_code), (self.book_name), (self.book_author))'