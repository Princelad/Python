from student import Student

class StudentManagementSystem:
    """Class to manage student records."""
    
    def __init__(self):
        """Initialize an empty student management system."""
        self.students = {}  # Dictionary to store students with ID as key
    
    def add_student(self, student_id, name, age, grade, courses=None):
        """Add a new student to the system."""
        if student_id in self.students:
            return False, "Student ID already exists"
        
        new_student = Student(student_id, name, age, grade, courses)
        self.students[student_id] = new_student
        return True, "Student added successfully"
    
    def update_student(self, student_id, name=None, age=None, grade=None):
        """Update an existing student's information."""
        if student_id not in self.students:
            return False, "Student not found"
        
        self.students[student_id].update_info(name, age, grade)
        return True, "Student information updated successfully"
    
    def delete_student(self, student_id):
        """Delete a student record."""
        if student_id not in self.students:
            return False, "Student not found"
        
        del self.students[student_id]
        return True, "Student deleted successfully"
    
    def get_all_students(self):
        """Return all students in the system."""
        return list(self.students.values())
    
    def search_by_id(self, student_id):
        """Search for a student by ID."""
        return self.students.get(student_id, None)
    
    def search_by_name(self, name):
        """Search for students by name (partial match)."""
        return [student for student in self.students.values()
                if name.lower() in student.name.lower()]
    
    def search_by_grade(self, grade):
        """Search for students by grade."""
        return [student for student in self.students.values()
                if student.grade == grade]
    
    def search_by_age(self, age):
        """Search for students by age."""
        return [student for student in self.students.values()
                if student.age == age]
    
    def search_by_course(self, course):
        """Search for students enrolled in a specific course."""
        return [student for student in self.students.values()
                if course in student.courses]
