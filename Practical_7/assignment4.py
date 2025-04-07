def read_five_words():
    """
    Reads a text file and prints any 5 words from the file.
    """
    # First create a sample text file if it doesn't exist
    sample_text = """This is a sample text file containing multiple words.
    Python is a great programming language for file operations.
    Reading and writing files in Python is relatively straightforward.
    This file contains more than five words for our example."""
    
    with open("sample_text.txt", "w") as file:
        file.write(sample_text)
    
    # Now read and print 5 words
    with open("sample_text.txt", "r") as file:
        content = file.read()
        words = content.split()
        
        # Print first 5 words
        print("First 5 words from the file:")
        for i in range(min(5, len(words))):
            print(f"{i+1}. {words[i]}")

if __name__ == "__main__":
    read_five_words()
