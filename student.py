class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, new_grade):
        self.grade = new_grade


if __name__ == "__main__":
    student = Student("Alice", 85)
    print(f"Student: {student.get_name()}")
    print(f"Grade: {student.get_grade()}")
    
    student.set_grade(90)
    print(f"Updated grade: {student.get_grade()}")
    
    student2 = Student("Bob", 92)
    print(f"Student 2: {student2.get_name()}")
    print(f"Student 2 Grade: {student2.get_grade()}")