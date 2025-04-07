class Student:
    """Class to represent a student in the management system."""
    
    def __init__(self, student_id, name, age, grade, courses=None):
        """Initialize a student with basic information."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = courses if courses else []
    
    def update_info(self, name=None, age=None, grade=None):
        """Update student information."""
        if name:
            self.name = name
        if age:
            self.age = age
        if grade:
            self.grade = grade
    
    def add_course(self, course):
        """Add a course to the student's course list."""
        if course not in self.courses:
            self.courses.append(course)
    
    def remove_course(self, course):
        """Remove a course from the student's course list."""
        if course in self.courses:
            self.courses.remove(course)
    
    def __str__(self):
        """Return string representation of the student."""
        return (f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, "
                f"Grade: {self.grade}, Courses: {', '.join(self.courses)}")
