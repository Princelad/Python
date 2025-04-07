import csv
import json
import os
from datetime import datetime

class FileHandler:
    @staticmethod
    def export_inventory_to_csv(bookstore, filename="inventory.csv"):
        """Export book inventory to CSV file"""
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['book_id', 'title', 'author', 'genre', 'price', 'type', 'quantity']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for item in bookstore.get_catalog():
                    book = item['book']
                    writer.writerow({
                        'book_id': book.book_id,
                        'title': book.title,
                        'author': book.author,
                        'genre': book.genre,
                        'price': book.calculate_price(),
                        'type': book.__class__.__name__,
                        'quantity': item['quantity']
                    })
            return True, f"Inventory exported to {filename}"
        except Exception as e:
            return False, f"Error exporting inventory: {str(e)}"
    
    @staticmethod
    def export_orders_to_json(bookstore, customer_id=None, filename=None):
        """Export orders to JSON file"""
        try:
            # Generate a default filename if not provided
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                if customer_id:
                    filename = f"orders_{customer_id}_{timestamp}.json"
                else:
                    filename = f"all_orders_{timestamp}.json"
            
            orders_data = []
            for order_id, order in bookstore._orders.items():
                # Filter by customer if specified
                if customer_id and order.customer.customer_id != customer_id:
                    continue
                
                # Build order data
                order_items = []
                for book, quantity in order.get_items():
                    order_items.append({
                        'book_id': book.book_id,
                        'title': book.title,
                        'quantity': quantity,
                        'price': book.calculate_price()
                    })
                
                orders_data.append({
                    'order_id': order.order_id,
                    'customer': {
                        'id': order.customer.customer_id,
                        'name': order.customer.name,
                        'email': order.customer.email
                    },
                    'date': order.order_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'status': order.status,
                    'items': order_items,
                    'total': order.calculate_total()
                })
            
            with open(filename, 'w') as f:
                json.dump(orders_data, f, indent=4)
            
            return True, f"Orders exported to {filename}"
        except Exception as e:
            return False, f"Error exporting orders: {str(e)}"
    
    @staticmethod
    def import_inventory_from_csv(bookstore, filename="inventory.csv"):
        """Import book inventory from CSV file"""
        try:
            from ..models.book import PrintedBook, EBook
            
            if not os.path.exists(filename):
                return False, f"File {filename} not found"
            
            books_added = 0
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        book_id = row['book_id']
                        title = row['title']
                        author = row['author']
                        genre = row['genre']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        book_type = row['type']
                        
                        # Create the appropriate book type
                        if book_type == 'PrintedBook':
                            book = PrintedBook(book_id, title, author, genre, price)
                        elif book_type == 'EBook':
                            book = EBook(book_id, title, author, genre, price)
                        else:
                            continue  # Skip unknown book types
                        
                        bookstore.add_book(book, quantity)
                        books_added += 1
                    except Exception as e:
                        print(f"Error importing row: {row}. Error: {e}")
                        continue
            
            return True, f"Successfully imported {books_added} books from {filename}"
        except Exception as e:
            return False, f"Error importing inventory: {str(e)}"
