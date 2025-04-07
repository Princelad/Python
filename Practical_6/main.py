import datetime
from pathlib import Path
import sys

# Add parent directory to path so we can import our modules
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

import mathutils
import shapemath

def main():
    # Display current date and time
    current_datetime = datetime.datetime.now()
    print("Current date and time:", current_datetime)
    
    # Format the date and time in a readable way
    formatted_date = current_datetime.strftime("%A, %B %d, %Y")
    formatted_time = current_datetime.strftime("%I:%M %p")
    print(f"Today is {formatted_date}")
    print(f"The time is {formatted_time}")
    
    print("\n--- Basic Arithmetic Operations ---")
    a, b = 10, 5
    print(f"Numbers: {a} and {b}")
    print(f"Addition: {mathutils.perform_arithmetic(a, b, 'add')}")
    print(f"Subtraction: {mathutils.perform_arithmetic(a, b, 'subtract')}")
    print(f"Multiplication: {mathutils.perform_arithmetic(a, b, 'multiply')}")
    print(f"Division: {mathutils.perform_arithmetic(a, b, 'divide')}")
    
    print("\n--- Even/Odd Check ---")
    numbers = [7, 12, 33, 84]
    for num in numbers:
        print(f"{num} is {mathutils.check_even_odd(num)}")
    
    print("\n--- Area Calculations ---")
    print(f"Area of circle with radius 5: {shapemath.calculate_area('circle', 5):.2f}")
    print(f"Area of rectangle with dimensions 4x6: {shapemath.calculate_area('rectangle', 4, 6)}")
    print(f"Area of triangle with base 8 and height 3: {shapemath.calculate_area('triangle', 8, 3)}")
    
    print("\n--- Prime Number Check ---")
    test_numbers = [2, 7, 10, 13, 25, 29]
    for num in test_numbers:
        print(f"{num} is {'prime' if shapemath.is_prime(num) else 'not prime'}")

if __name__ == "__main__":
    main()
