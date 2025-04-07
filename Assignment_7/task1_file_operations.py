"""
Task 1: Write a program that creates a new file, writes some content to it, closes the file, 
and then reopens it to read and display the content.
"""

def main():
    # Create a new file and write to it
    with open("sample_file.txt", "w") as file:
        file.write("Hello, this is line 1!\n")
        file.write("This is line 2 of our file.\n")
        file.write("And this is the third line of content.\n")
        print("Content has been written to sample_file.txt")
    
    # Reopen the file and read its content
    print("\nReading content from file:")
    with open("sample_file.txt", "r") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    main()
