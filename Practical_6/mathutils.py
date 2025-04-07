def perform_arithmetic(a, b, operation):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'
        
    Returns:
        float: Result of the operation
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'")

def check_even_odd(number):
    """
    Check if a number is even or odd.
    
    Args:
        number (int): The number to check
        
    Returns:
        str: 'even' or 'odd'
    """
    if isinstance(number, int):
        return 'even' if number % 2 == 0 else 'odd'
    else:
        raise TypeError("Input must be an integer")
