import datetime

class Order:
    def __init__(self, order_id, customer):
        self._order_id = order_id
        self._customer = customer
        self._items = []  # List of tuples (book, quantity)
        self._order_date = datetime.datetime.now()
        self._status = "Pending"
    
    @property
    def order_id(self):
        return self._order_id
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def order_date(self):
        return self._order_date
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Canceled"]
        if new_status in valid_statuses:
            self._status = new_status
        else:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
    
    def add_book(self, book, quantity=1):
        self._items.append((book, quantity))
    
    def remove_book(self, book_id):
        for i, (book, _) in enumerate(self._items):
            if book.book_id == book_id:
                del self._items[i]
                return True
        return False
    
    def update_quantity(self, book_id, quantity):
        for i, (book, _) in enumerate(self._items):
            if book.book_id == book_id:
                if quantity <= 0:
                    del self._items[i]
                else:
                    self._items[i] = (book, quantity)
                return True
        return False
    
    def calculate_total(self):
        return sum(book.calculate_price() * qty for book, qty in self._items)
    
    def get_items(self):
        return [(book, qty) for book, qty in self._items]
    
    def finalize_order(self):
        self._customer.add_to_order_history(self)
        self.status = "Processing"
        return self.calculate_total()
    
    def __str__(self):
        item_list = "\n".join([f"- {book.title} (x{qty}): ${book.calculate_price() * qty:.2f}" 
                              for book, qty in self._items])
        return (f"Order #{self.order_id}\n"
                f"Customer: {self.customer.name}\n"
                f"Date: {self.order_date.strftime('%Y-%m-%d %H:%M')}\n"
                f"Status: {self.status}\n"
                f"Items:\n{item_list}\n"
                f"Total: ${self.calculate_total():.2f}")
    
    @classmethod
    def from_db_data(cls, order_data, items_data, customers_dict=None, books_dict=None):
        """Create an Order instance from database data"""
        from .book import Book
        from .customer import Customer
        
        if order_data is None:
            return None
        
        # Get or create the customer
        if customers_dict and order_data['customer_id'] in customers_dict:
            customer = customers_dict[order_data['customer_id']]
        else:
            # This would require another database query in practice
            customer = Customer(
                order_data['customer_id'], 
                "Unknown", 
                "unknown@example.com", 
                "Unknown Address"
            )
        
        # Create the order
        order = cls(order_data['order_id'], customer)
        
        # Parse order date if it's a string
        if isinstance(order_data['order_date'], str):
            try:
                order._order_date = datetime.datetime.strptime(
                    order_data['order_date'], '%Y-%m-%d %H:%M:%S'
                )
            except ValueError:
                # Keep the default date if parsing fails
                pass
        
        # Set status
        order._status = order_data['status']
        
        # Add items
        for item in items_data:
            # Get or create the book
            if books_dict and item['book_id'] in books_dict:
                book = books_dict[item['book_id']]
            else:
                book = Book.from_db_row(item)
            
            if book:
                order.add_book(book, item['quantity'])
        
        return order