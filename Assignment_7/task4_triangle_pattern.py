"""
Task 5: Write a program that generates a triangle pattern of 5 rows 
and saves the pattern into a file named triangle.txt.
"""

def main():
    try:
        with open("triangle.txt", "w") as file:
            # Generate and write a triangle pattern of 5 rows
            for i in range(1, 6):
                line = "*" * i
                file.write(line + "\n")
            
            print("Triangle pattern has been saved to triangle.txt")
        
        # Display the content of the file
        print("\nContent of triangle.txt:")
        with open("triangle.txt", "r") as file:
            print(file.read())
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
