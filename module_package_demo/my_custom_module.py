"""
A custom module providing simple utility functions.

This module demonstrates how to create and use a custom module in Python.
"""

MODULE_VERSION = "1.0.0"

def add_numbers(a, b):
    """Add two numbers together and return the result."""
    return a + b

def subtract_numbers(a, b):
    """Subtract b from a and return the result."""
    return a - b

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# This code executes when the module is run directly
if __name__ == "__main__":
    print("This module provides math utility functions.")
    print(f"Version: {MODULE_VERSION}")
