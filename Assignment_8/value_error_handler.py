def convert_to_integer(string_value):
    """
    Converts a string to an integer.
    Raises ValueError if the string is not a valid integer.
    """
    return int(string_value)

def main():
    print("String to Integer Converter Program")
    
    while True:
        try:
            user_input = input("Enter a number to convert to integer (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                print("Exiting program...")
                break
                
            number = convert_to_integer(user_input)
            print(f"Successfully converted to integer: {number}")
            print(f"Type of the converted value: {type(number)}")
            
        except ValueError:
            print("Error: The input is not a valid integer. Please try again.")
        
        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()
