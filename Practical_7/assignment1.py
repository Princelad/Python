def create_write_read():
    """
    Creates a new file, writes content to it, closes the file, 
    and then reopens it to read and display the content.
    """
    # Creating and writing to the file
    print("Creating and writing to a file...")
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.write("This is the third line.\n")
        file.write("This is the fourth line.\n")
        file.write("This is the fifth line.\n")
    
    # Reopening the file to read its content
    print("\nReading the file content:")
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    create_write_read()
