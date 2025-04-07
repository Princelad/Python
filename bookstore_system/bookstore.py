from .models.order import Order

class Bookstore:
    def __init__(self, name):
        self._name = name
        self._book_inventory = {}  # book_id -> (book, quantity)
        self._customers = {}  # customer_id -> customer
        self._orders = {}  # order_id -> order
        self._next_order_id = 1000
    
    @property
    def name(self):
        return self._name
    
    def add_book(self, book, quantity=1):
        if book.book_id in self._book_inventory:
            _, current_qty = self._book_inventory[book.book_id]
            self._book_inventory[book.book_id] = (book, current_qty + quantity)
        else:
            self._book_inventory[book.book_id] = (book, quantity)
    
    def remove_book(self, book_id, quantity=1):
        if book_id in self._book_inventory:
            book, current_qty = self._book_inventory[book_id]
            if quantity >= current_qty:
                del self._book_inventory[book_id]
            else:
                self._book_inventory[book_id] = (book, current_qty - quantity)
            return True
        return False
    
    def get_book(self, book_id):
        if book_id in self._book_inventory:
            book, _ = self._book_inventory[book_id]
            return book
        return None
    
    def get_book_quantity(self, book_id):
        if book_id in self._book_inventory:
            _, quantity = self._book_inventory[book_id]
            return quantity
        return 0
    
    def register_customer(self, customer):
        self._customers[customer.customer_id] = customer
    
    def get_customer(self, customer_id):
        return self._customers.get(customer_id)
    
    def create_order(self, customer_id):
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError(f"Customer with ID {customer_id} not found")
        
        order_id = self._next_order_id
        self._next_order_id += 1
        
        order = Order(order_id, customer)
        self._orders[order_id] = order
        return order
    
    def process_order(self, order_id):
        if order_id not in self._orders:
            raise ValueError(f"Order with ID {order_id} not found")
        
        order = self._orders[order_id]
        
        # Check inventory availability
        for book, qty in order.get_items():
            if self.get_book_quantity(book.book_id) < qty:
                raise ValueError(f"Insufficient inventory for book: {book.title}")
        
        # Update inventory
        for book, qty in order.get_items():
            self.remove_book(book.book_id, qty)
        
        # Finalize the order
        total = order.finalize_order()
        return total
    
    def get_catalog(self):
        catalog = []
        for book_id, (book, quantity) in self._book_inventory.items():
            catalog.append({
                "book": book,
                "quantity": quantity,
                "price": book.calculate_price()
            })
        return catalog
    
    def search_books(self, keyword=None, genre=None, author=None):
        results = []
        for book_id, (book, quantity) in self._book_inventory.items():
            if ((keyword is None or keyword.lower() in book.title.lower()) and
                (genre is None or genre.lower() == book.genre.lower()) and
                (author is None or author.lower() in book.author.lower())):
                results.append({
                    "book": book,
                    "quantity": quantity,
                    "price": book.calculate_price()
                })
        return results
    
    def calculate_total_revenue(self):
        return sum(order.calculate_total() for order in self._orders.values() 
                 if order.status not in ["Pending", "Canceled"])
    
    def __str__(self):
        return f"{self.name} Bookstore - {len(self._book_inventory)} books, {len(self._customers)} customers"