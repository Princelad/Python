def access_list_element(my_list, index):
    """
    Tries to access an element in a list at the given index.
    Returns the element if successful, otherwise raises IndexError.
    """
    return my_list[index]

def main():
    # Sample list to work with
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("List Element Access Program")
    print(f"Available list: {fruits}")
    print(f"Valid indices: 0 to {len(fruits) - 1}\n")
    
    while True:
        try:
            user_input = input("Enter an index to access (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                print("Exiting program...")
                break
                
            index = int(user_input)
            element = access_list_element(fruits, index)
            print(f"Element at index {index}: {element}")
            
        except ValueError:
            print("Error: Please enter a valid integer for the index")
        except IndexError:
            print(f"Error: Index out of range. Please enter an index between 0 and {len(fruits) - 1}")
        
        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()
