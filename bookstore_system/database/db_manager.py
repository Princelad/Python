import sqlite3
import os
import datetime

class DatabaseManager:
    def __init__(self, db_path='bookstore.db'):
        """Initialize database connection and setup tables if they don't exist"""
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.connect()
        self.setup_tables()
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return False
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
    
    def commit(self):
        """Commit changes to database"""
        if self.connection:
            self.connection.commit()
    
    def setup_tables(self):
        """Create necessary tables if they don't exist"""
        try:
            # Books table
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                base_price REAL NOT NULL,
                book_type TEXT NOT NULL,
                additional_info TEXT,
                quantity INTEGER DEFAULT 0
            )
            ''')
            
            # Customers table
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                address TEXT NOT NULL,
                payment_details TEXT
            )
            ''')
            
            # Orders table
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id TEXT NOT NULL,
                order_date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
            )
            ''')
            
            # Order items table
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                book_id TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (order_id),
                FOREIGN KEY (book_id) REFERENCES books (book_id)
            )
            ''')
            
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error setting up tables: {e}")
            return False
    
    # Book related operations
    def add_book(self, book, quantity=1):
        """Add a new book to the database or update quantity if it exists"""
        try:
            # Additional info will be serialized differently based on book type
            if book.__class__.__name__ == 'PrintedBook':
                book_type = 'Printed'
                additional_info = f"{book.shipping_cost},{book.pages}"
            elif book.__class__.__name__ == 'EBook':
                book_type = 'EBook'
                additional_info = f"{book.file_size_mb},{book.discount}"
            else:
                book_type = 'Unknown'
                additional_info = ""
            
            # Check if book exists
            self.cursor.execute("SELECT quantity FROM books WHERE book_id = ?", (book.book_id,))
            result = self.cursor.fetchone()
            
            if result:
                # Update quantity
                new_qty = result['quantity'] + quantity
                self.cursor.execute(
                    "UPDATE books SET quantity = ? WHERE book_id = ?", 
                    (new_qty, book.book_id)
                )
            else:
                # Insert new book
                self.cursor.execute(
                    "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (book.book_id, book.title, book.author, book.genre, book.base_price, 
                     book_type, additional_info, quantity)
                )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error adding book: {e}")
            return False
    
    def remove_book(self, book_id, quantity=1):
        """Remove or reduce quantity of a book"""
        try:
            self.cursor.execute("SELECT quantity FROM books WHERE book_id = ?", (book_id,))
            result = self.cursor.fetchone()
            
            if not result:
                return False
            
            current_qty = result['quantity']
            
            if quantity >= current_qty:
                self.cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
            else:
                self.cursor.execute(
                    "UPDATE books SET quantity = ? WHERE book_id = ?", 
                    (current_qty - quantity, book_id)
                )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error removing book: {e}")
            return False
    
    def get_all_books(self):
        """Retrieve all books from the database"""
        try:
            self.cursor.execute("SELECT * FROM books")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error getting books: {e}")
            return []
    
    def get_book(self, book_id):
        """Get a single book by its ID"""
        try:
            self.cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error getting book: {e}")
            return None
    
    def search_books(self, keyword=None, genre=None, author=None):
        """Search books based on various criteria"""
        try:
            query = "SELECT * FROM books WHERE 1=1"
            params = []
            
            if keyword:
                query += " AND title LIKE ?"
                params.append(f"%{keyword}%")
            
            if genre:
                query += " AND genre LIKE ?"
                params.append(f"%{genre}%")
                
            if author:
                query += " AND author LIKE ?"
                params.append(f"%{author}%")
            
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error searching books: {e}")
            return []
    
    # Customer related operations
    def add_customer(self, customer):
        """Add a new customer or update existing one"""
        try:
            # Check if customer exists
            self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer.customer_id,))
            if self.cursor.fetchone():
                # Update existing customer
                self.cursor.execute(
                    "UPDATE customers SET name = ?, email = ?, address = ? WHERE customer_id = ?",
                    (customer.name, customer.email, customer.address, customer.customer_id)
                )
            else:
                # Insert new customer
                payment_details = None  # We'll store this separately for security
                self.cursor.execute(
                    "INSERT INTO customers VALUES (?, ?, ?, ?, ?)",
                    (customer.customer_id, customer.name, customer.email, customer.address, payment_details)
                )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error adding customer: {e}")
            return False
    
    def get_customer(self, customer_id):
        """Get a customer by ID"""
        try:
            self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error getting customer: {e}")
            return None
    
    def get_all_customers(self):
        """Get all customers"""
        try:
            self.cursor.execute("SELECT * FROM customers")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error getting customers: {e}")
            return []
    
    # Order related operations
    def create_order(self, order):
        """Create a new order in database"""
        try:
            date_str = order.order_date.strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute(
                "INSERT INTO orders VALUES (?, ?, ?, ?)",
                (order.order_id, order.customer.customer_id, date_str, order.status)
            )
            
            # Add order items
            for book, quantity in order.get_items():
                self.cursor.execute(
                    "INSERT INTO order_items (order_id, book_id, quantity) VALUES (?, ?, ?)",
                    (order.order_id, book.book_id, quantity)
                )
            
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error creating order: {e}")
            return False
    
    def get_order(self, order_id):
        """Get an order and its items by ID"""
        try:
            self.cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
            order_data = self.cursor.fetchone()
            if not order_data:
                return None
            
            # Get all items for this order
            self.cursor.execute(
                "SELECT oi.book_id, oi.quantity, b.* FROM order_items oi "
                "JOIN books b ON oi.book_id = b.book_id "
                "WHERE oi.order_id = ?", (order_id,)
            )
            items = self.cursor.fetchall()
            
            return {
                "order": order_data,
                "items": items
            }
        except sqlite3.Error as e:
            print(f"Database error getting order: {e}")
            return None
    
    def update_order_status(self, order_id, status):
        """Update an order's status"""
        try:
            self.cursor.execute(
                "UPDATE orders SET status = ? WHERE order_id = ?",
                (status, order_id)
            )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error updating order status: {e}")
            return False
    
    def get_customer_orders(self, customer_id):
        """Get all orders for a specific customer"""
        try:
            self.cursor.execute(
                "SELECT * FROM orders WHERE customer_id = ? ORDER BY order_date DESC",
                (customer_id,)
            )
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error getting customer orders: {e}")
            return []
