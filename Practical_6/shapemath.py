import math

def calculate_area(shape, *args):
    """
    Calculate the area of different shapes.
    
    Args:
        shape (str): The shape type ('circle', 'rectangle', or 'triangle')
        *args: Dimensions of the shape
            - For circle: radius
            - For rectangle: length, width
            - For triangle: base, height
            
    Returns:
        float: The calculated area
    """
    if shape == 'circle':
        if len(args) != 1:
            raise ValueError("Circle requires exactly one argument (radius)")
        radius = args[0]
        return math.pi * radius ** 2
    
    elif shape == 'rectangle':
        if len(args) != 2:
            raise ValueError("Rectangle requires exactly two arguments (length and width)")
        length, width = args
        return length * width
    
    elif shape == 'triangle':
        if len(args) != 2:
            raise ValueError("Triangle requires exactly two arguments (base and height)")
        base, height = args
        return 0.5 * base * height
    
    else:
        raise ValueError("Unsupported shape. Choose 'circle', 'rectangle', or 'triangle'")

def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if not isinstance(number, int) or number < 2:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
