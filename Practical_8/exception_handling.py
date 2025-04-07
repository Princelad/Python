import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Practical_6.shapemath import calculate_area

def demonstrate_basic_exception():
    """Demonstrate basic try-except block for handling exceptions."""
    try:
        # Attempting to divide by zero will raise a ZeroDivisionError
        result = 10 / 0
        print(f"Result: {result}")  # This line won't execute
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

def demonstrate_multiple_exceptions():
    """Demonstrate handling different types of exceptions with multiple except blocks."""
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        result = 100 / number
        print(f"100 divided by {number} is {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

def demonstrate_else_clause():
    """Demonstrate the use of else clause in exception handling."""
    try:
        shape = input("Enter a shape (circle, rectangle, or triangle): ").lower()
        if shape == 'circle':
            radius = float(input("Enter radius: "))
            dimensions = [radius]
        elif shape == 'rectangle':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            dimensions = [length, width]
        elif shape == 'triangle':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            dimensions = [base, height]
        else:
            raise ValueError(f"Unsupported shape: {shape}")
    except ValueError as e:
        print(f"Input error: {e}")
    else:
        # This block runs if no exceptions were raised in the try block
        area = calculate_area(shape, *dimensions)
        print(f"The area of the {shape} is {area:.2f} square units.")

def demonstrate_finally_clause():
    """Demonstrate the use of finally clause in exception handling."""
    file = None
    try:
        filename = input("Enter filename to read: ")
        file = open(filename, 'r')
        content = file.read()
        print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print("Error: Could not read the file.")
    finally:
        # This block always executes, whether an exception occurred or not
        if file is not None:
            file.close()
            print("File has been closed.")
        print("File operation attempt completed.")

def demonstrate_raise_statement():
    """Demonstrate raising exceptions manually."""
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            raise PermissionError("You must be at least 18 years old.")
        print(f"Your age is {age}.")
    except ValueError as e:
        print(f"Invalid age: {e}")
    except PermissionError as e:
        print(f"Access denied: {e}")

def main():
    """Run all exception handling demonstrations."""
    print("\n1. Basic Exception Handling:")
    demonstrate_basic_exception()
    
    print("\n2. Multiple Exception Types:")
    demonstrate_multiple_exceptions()
    
    print("\n3. Using Else Clause:")
    demonstrate_else_clause()
    
    print("\n4. Using Finally Clause:")
    demonstrate_finally_clause()
    
    print("\n5. Raising Exceptions:")
    demonstrate_raise_statement()

if __name__ == "__main__":
    main()
