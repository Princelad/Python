# SQLite Database Operations

This project demonstrates how to perform basic SQLite database operations in Python.

## Features

- Database connection establishment
- Creating tables
- Inserting data
- Selecting data (fetchone, fetchall, fetchmany)
- Updating records
- Deleting records
- Exception handling for database operations

## Files

- `db_operations.py` - Contains the DatabaseManager class with all database operation methods
- `main.py` - Demonstrates how to use the DatabaseManager class

## How to Run

```bash
python main.py
```

## Operations Demonstrated

1. **Connection** - Establishing a connection to an SQLite database
2. **Table Creation** - Creating an employees table with various field types
3. **Data Insertion** - Adding employee records to the database
4. **Data Retrieval** - Three different methods:
   - `fetchall()` - Retrieves all records
   - `fetchone()` - Retrieves a single record
   - `fetchmany()` - Retrieves a specified number of records
5. **Data Update** - Modifying existing records
6. **Data Deletion** - Removing records from the database
7. **Connection Closing** - Properly closing the database connection

All operations include proper error handling using try-except blocks.
