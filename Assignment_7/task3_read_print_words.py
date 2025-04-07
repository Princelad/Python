"""
Task 4: Write a program that reads a text file and prints any 5 words from the file.
"""

def main():
    # First create a sample file
    with open("sample_text.txt", "w") as file:
        file.write("This is a sample text file with multiple words for our program to read. ")
        file.write("It contains enough words to demonstrate the task of reading and displaying ")
        file.write("a specific number of words from a file.")
    
    try:
        # Open and read the file
        with open("sample_text.txt", "r") as file:
            content = file.read()
            words = content.split()
            
            if len(words) >= 5:
                print("First 5 words from the file:")
                for i in range(5):
                    print(f"{i+1}: {words[i]}")
            else:
                print("The file contains less than 5 words.")
                print(f"Words in the file: {words}")
    
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")

if __name__ == "__main__":
    main()
