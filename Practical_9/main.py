from db_operations import DatabaseManager

def main():
    # Create a database manager instance
    db = DatabaseManager("employees.db")
    
    # Create table
    db.create_table()
    
    # Insert sample data
    print("\n--- Inserting Data ---")
    db.insert_data("John Doe", "Software Engineer", 75000.00, "2022-01-15")
    db.insert_data("Jane Smith", "Project Manager", 85000.00, "2021-05-10")
    db.insert_data("Michael Johnson", "Data Analyst", 65000.00, "2022-03-22")
    db.insert_data("Emily Brown", "UX Designer", 70000.00, "2021-11-08")
    db.insert_data("Robert Wilson", "DevOps Engineer", 80000.00, "2022-02-14")
    
    # Select and display all data
    print("\n--- Selecting All Data ---")
    db.select_all_data()
    
    # Select a single employee
    print("\n--- Selecting One Employee ---")
    db.select_one_employee(2)
    
    # Select multiple employees
    print("\n--- Selecting Multiple Employees ---")
    db.select_many_employees(3)
    
    # Update data
    print("\n--- Updating Data ---")
    db.update_data(1, 78000.00)
    db.select_one_employee(1)
    
    # Delete data
    print("\n--- Deleting Data ---")
    db.delete_data(5)
    db.select_all_data()
    
    # Close the connection
    db.close_connection()

if __name__ == "__main__":
    main()
