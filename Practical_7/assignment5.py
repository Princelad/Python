def generate_triangle():
    """
    Generates a triangle pattern of 5 rows and saves it in triangle.txt.
    """
    # Generate the triangle pattern
    triangle = ""
    for i in range(1, 6):
        triangle += "*" * i + "\n"
    
    # Save the pattern to triangle.txt
    with open("triangle.txt", "w") as file:
        file.write(triangle)
    
    print("Triangle pattern has been saved to triangle.txt")
    
    # Display the triangle pattern
    print("\nTriangle pattern:")
    with open("triangle.txt", "r") as file:
        print(file.read())

if __name__ == "__main__":
    generate_triangle()
