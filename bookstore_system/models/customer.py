class Customer:
    def __init__(self, customer_id, name, email, address):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._address = address
        self._payment_details = None
        self._order_history = []
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def address(self):
        return self._address
    
    def set_payment_details(self, payment_details):
        # Securely store payment details (in a real system, this would be encrypted)
        self._payment_details = payment_details
    
    def get_payment_details_last_four(self):
        # Only return the last 4 digits of payment card for security
        if self._payment_details and 'card_number' in self._payment_details:
            return f"****-****-****-{self._payment_details['card_number'][-4:]}"
        return None
    
    def add_to_order_history(self, order):
        self._order_history.append(order)
    
    def get_order_history(self):
        # Return a copy to prevent direct modification
        return self._order_history.copy()
    
    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"
    
    @classmethod
    def from_db_row(cls, row):
        """Create a Customer instance from a database row"""
        if row is None:
            return None
            
        customer = cls(
            row['customer_id'],
            row['name'],
            row['email'],
            row['address']
        )
        
        # Handle payment details if they exist
        if row['payment_details']:
            try:
                import json
                payment_details = json.loads(row['payment_details'])
                customer.set_payment_details(payment_details)
            except Exception:
                # If we can't parse payment details, just leave them as None
                pass
                
        return customer