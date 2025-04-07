def separate_odd_even():
    """
    Reads a list of numbers, inserts odd numbers into odd_numbers.txt,
    and even numbers into even_numbers.txt.
    """
    # Get numbers from the user
    numbers_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in numbers_input.split()]
    
    # Open files for odd and even numbers
    with open("odd_numbers.txt", "w") as odd_file, open("even_numbers.txt", "w") as even_file:
        for num in numbers:
            if num % 2 == 0:  # Even number
                even_file.write(f"{num}\n")
            else:  # Odd number
                odd_file.write(f"{num}\n")
    
    # Display the results
    print("\nNumbers have been sorted into odd_numbers.txt and even_numbers.txt")
    
    # Reading and displaying odd numbers
    print("\nOdd numbers:")
    with open("odd_numbers.txt", "r") as odd_file:
        print(odd_file.read())
    
    # Reading and displaying even numbers
    print("Even numbers:")
    with open("even_numbers.txt", "r") as even_file:
        print(even_file.read())

if __name__ == "__main__":
    separate_odd_even()
