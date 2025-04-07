import os

def basic_file_operations():
    """Demonstrates basic file operations in Python."""
    
    # Writing to a file
    print("Writing to a file...")
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a test file.\n")
        file.write("This is the second line.\n")
        file.writelines(["Third line.\n", "Fourth line.\n"])
    
    # Reading from a file
    print("\nReading the entire file at once:")
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
    
    # Reading line by line
    print("\nReading line by line:")
    with open("sample.txt", "r") as file:
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()
    
    # Reading all lines into a list
    print("\nReading all lines into a list:")
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(lines)
    
    # Appending to a file
    print("\nAppending to the file...")
    with open("sample.txt", "a") as file:
        file.write("This line was appended.\n")
    
    # Reading the file after append
    print("\nReading file after append:")
    with open("sample.txt", "r") as file:
        print(file.read())
    
    # File position operations
    print("\nFile position operations:")
    with open("sample.txt", "r") as file:
        print(f"Current position: {file.tell()}")
        print(file.read(10))  # Read 10 characters
        print(f"New position: {file.tell()}")
        file.seek(0)  # Go back to the beginning
        print(f"After seek(0): {file.tell()}")
        print(file.read(5))
    
    # File existence check
    print("\nFile exists check:")
    print(f"'sample.txt' exists: {os.path.exists('sample.txt')}")
    print(f"'nonexistent.txt' exists: {os.path.exists('nonexistent.txt')}")
    
    # File renaming
    print("\nRenaming file...")
    if os.path.exists("renamed.txt"):
        os.remove("renamed.txt")  # Remove if exists to avoid errors
    os.rename("sample.txt", "renamed.txt")
    print(f"'sample.txt' exists: {os.path.exists('sample.txt')}")
    print(f"'renamed.txt' exists: {os.path.exists('renamed.txt')}")
    
    # Getting file path
    print("\nFile path:")
    print(f"Absolute path: {os.path.abspath('renamed.txt')}")
    print(f"Directory name: {os.path.dirname(os.path.abspath('renamed.txt'))}")
    
    # File removal
    print("\nRemoving file...")
    os.remove("renamed.txt")
    print(f"'renamed.txt' exists: {os.path.exists('renamed.txt')}")

if __name__ == "__main__":
    basic_file_operations()
