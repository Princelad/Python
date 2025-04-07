from student_management import StudentManagementSystem

def print_menu():
    """Display the main menu options."""
    print("\n===== Student Management System =====")
    print("1. Add a new student")
    print("2. Update student information")
    print("3. Delete a student")
    print("4. Display all students")
    print("5. Search students")
    print("0. Exit")
    print("=====================================")

def get_search_option():
    """Display and get search options."""
    print("\n----- Search Options -----")
    print("1. Search by ID")
    print("2. Search by name")
    print("3. Search by age")
    print("4. Search by grade")
    print("5. Search by course")
    print("0. Back to main menu")
    print("--------------------------")
    return input("Enter your choice: ")

def print_students(students):
    """Display a list of students."""
    if not students:
        print("No students found.")
        return
    
    print("\n----- Student List -----")
    for student in students:
        print(student)
    print("------------------------")

def main():
    """Main function to run the Student Management System."""
    sms = StudentManagementSystem()
    
    # Add some sample data
    sms.add_student("S001", "John Doe", 20, "A", ["Math", "Science"])
    sms.add_student("S002", "Jane Smith", 19, "B", ["History", "English"])
    sms.add_student("S003", "Bob Johnson", 21, "A", ["Physics", "Chemistry"])
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Add a new student
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue
                
            grade = input("Enter grade: ")
            courses = input("Enter courses (comma separated): ").split(',')
            courses = [course.strip() for course in courses if course.strip()]
            
            success, message = sms.add_student(student_id, name, age, grade, courses)
            print(message)
            
        elif choice == '2':
            # Update student information
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave empty to keep current): ")
            name = name if name else None
            
            age = None
            age_input = input("Enter new age (leave empty to keep current): ")
            if age_input:
                try:
                    age = int(age_input)
                except ValueError:
                    print("Invalid age. Update canceled.")
                    continue
            
            grade = input("Enter new grade (leave empty to keep current): ")
            grade = grade if grade else None
            
            success, message = sms.update_student(student_id, name, age, grade)
            print(message)
            
        elif choice == '3':
            # Delete a student
            student_id = input("Enter student ID to delete: ")
            success, message = sms.delete_student(student_id)
            print(message)
            
        elif choice == '4':
            # Display all students
            students = sms.get_all_students()
            print_students(students)
            
        elif choice == '5':
            # Search students
            while True:
                search_choice = get_search_option()
                
                if search_choice == '1':
                    student_id = input("Enter student ID: ")
                    student = sms.search_by_id(student_id)
                    if student:
                        print_students([student])
                    else:
                        print("No student found with that ID.")
                
                elif search_choice == '2':
                    name = input("Enter name to search: ")
                    students = sms.search_by_name(name)
                    print_students(students)
                
                elif search_choice == '3':
                    try:
                        age = int(input("Enter age to search: "))
                        students = sms.search_by_age(age)
                        print_students(students)
                    except ValueError:
                        print("Invalid age. Please enter a number.")
                
                elif search_choice == '4':
                    grade = input("Enter grade to search: ")
                    students = sms.search_by_grade(grade)
                    print_students(students)
                
                elif search_choice == '5':
                    course = input("Enter course to search: ")
                    students = sms.search_by_course(course)
                    print_students(students)
                
                elif search_choice == '0':
                    break
                
                else:
                    print("Invalid choice. Please try again.")
            
        elif choice == '0':
            # Exit the program
            print("Thank you for using the Student Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
