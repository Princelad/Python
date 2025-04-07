from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, book_id, title, author, genre, base_price):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._genre = genre
        self._base_price = base_price
    
    @property
    def book_id(self):
        return self._book_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def base_price(self):
        return self._base_price
    
    @abstractmethod
    def calculate_price(self):
        pass
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}) - ${self.calculate_price():.2f}"
    
    @classmethod
    def from_db_row(cls, row):
        """Factory method to create a Book instance from database row"""
        if row is None:
            return None
            
        book_id = row['book_id']
        title = row['title']
        author = row['author']
        genre = row['genre']
        base_price = row['base_price']
        book_type = row['book_type']
        additional_info = row['additional_info'].split(',') if row['additional_info'] else []
        
        if book_type == 'Printed':
            shipping_cost = float(additional_info[0]) if additional_info else 2.0
            pages = int(additional_info[1]) if len(additional_info) > 1 else 0
            return PrintedBook(book_id, title, author, genre, base_price, shipping_cost, pages)
        elif book_type == 'EBook':
            file_size = float(additional_info[0]) if additional_info else 0
            discount = float(additional_info[1]) if len(additional_info) > 1 else 0.2
            return EBook(book_id, title, author, genre, base_price, file_size, discount)
        else:
            # Default fallback, should not happen with proper data
            return None


class PrintedBook(Book):
    def __init__(self, book_id, title, author, genre, base_price, shipping_cost=2.0, pages=0):
        super().__init__(book_id, title, author, genre, base_price)
        self._shipping_cost = shipping_cost
        self._pages = pages
    
    @property
    def shipping_cost(self):
        return self._shipping_cost
    
    @property
    def pages(self):
        return self._pages
    
    def calculate_price(self):
        return self.base_price + self.shipping_cost


class EBook(Book):
    def __init__(self, book_id, title, author, genre, base_price, file_size_mb=0, discount=0.2):
        super().__init__(book_id, title, author, genre, base_price)
        self._file_size_mb = file_size_mb
        self._discount = discount
    
    @property
    def file_size_mb(self):
        return self._file_size_mb
    
    @property
    def discount(self):
        return self._discount
    
    def calculate_price(self):
        # E-books are typically cheaper (discount applied)
        return self.base_price * (1 - self.discount)