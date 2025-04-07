import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="example.db"):
        """Initialize database connection"""
        try:
            # Create database directory if it doesn't exist
            os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
            
            # Connect to database
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            print(f"Successfully connected to {db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query, params=None):
        """Execute an SQL query with exception handling"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return True
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return False

    def create_table(self):
        """Create a new table in the database"""
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL,
            hire_date TEXT
        )
        '''
        if self.execute_query(create_table_query):
            print("Table created successfully")
        
    def insert_data(self, name, position, salary, hire_date):
        """Insert data into the employees table"""
        insert_query = '''
        INSERT INTO employees (name, position, salary, hire_date)
        VALUES (?, ?, ?, ?)
        '''
        params = (name, position, salary, hire_date)
        
        if self.execute_query(insert_query, params):
            self.connection.commit()
            print(f"Successfully inserted data for {name}")
    
    def select_all_data(self):
        """Select all data from the employees table using fetchall()"""
        try:
            self.cursor.execute("SELECT * FROM employees")
            rows = self.cursor.fetchall()
            
            print("\nAll employees:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}, Hire Date: {row[4]}")
            
            return rows
        except sqlite3.Error as e:
            print(f"Error selecting data: {e}")
            return []
    
    def select_one_employee(self, employee_id):
        """Select data for a single employee using fetchone()"""
        try:
            self.cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
            employee = self.cursor.fetchone()
            
            if employee:
                print(f"\nEmployee details:")
                print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}")
                print(f"Salary: {employee[3]}, Hire Date: {employee[4]}")
                return employee
            else:
                print(f"No employee found with ID {employee_id}")
                return None
        except sqlite3.Error as e:
            print(f"Error selecting employee: {e}")
            return None

    def select_many_employees(self, limit=2):
        """Select multiple employees using fetchmany()"""
        try:
            self.cursor.execute("SELECT * FROM employees")
            employees = self.cursor.fetchmany(limit)
            
            print(f"\nFirst {limit} employees:")
            for employee in employees:
                print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}")
            
            return employees
        except sqlite3.Error as e:
            print(f"Error selecting employees: {e}")
            return []

    def update_data(self, employee_id, new_salary):
        """Update employee salary by ID"""
        update_query = "UPDATE employees SET salary = ? WHERE id = ?"
        params = (new_salary, employee_id)
        
        if self.execute_query(update_query, params):
            self.connection.commit()
            print(f"Successfully updated salary for employee ID {employee_id}")
    
    def delete_data(self, employee_id):
        """Delete an employee by ID"""
        delete_query = "DELETE FROM employees WHERE id = ?"
        
        if self.execute_query(delete_query, (employee_id,)):
            self.connection.commit()
            print(f"Successfully deleted employee with ID {employee_id}")
    
    def close_connection(self):
        """Close the database connection"""
        try:
            self.connection.close()
            print("Database connection closed")
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")
