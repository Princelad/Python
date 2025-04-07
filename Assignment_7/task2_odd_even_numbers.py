"""
Task 2: Write a program that reads a list of numbers, inserts odd numbers into a file named 
odd_numbers.txt, and even numbers into a file named even_numbers.txt.
"""

def main():
    # Get input numbers from the user
    try:
        numbers_input = input("Enter numbers separated by spaces: ")
        numbers = [int(num) for num in numbers_input.split()]
        
        # Open the files for writing
        with open("odd_numbers.txt", "w") as odd_file, open("even_numbers.txt", "w") as even_file:
            odd_count = even_count = 0
            
            for num in numbers:
                if num % 2 == 0:  # Even number
                    even_file.write(f"{num}\n")
                    even_count += 1
                else:  # Odd number
                    odd_file.write(f"{num}\n")
                    odd_count += 1
        
        print(f"Wrote {odd_count} odd numbers to odd_numbers.txt")
        print(f"Wrote {even_count} even numbers to even_numbers.txt")
        
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
