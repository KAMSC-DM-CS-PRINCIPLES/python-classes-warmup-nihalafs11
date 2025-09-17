from student import Student

def test_student_creation():
    """Test creating a student with name and grade"""
    student = Student("Alice", 85)
    assert student.get_name() == "Alice"
    assert student.get_grade() == 85

def test_student_get_name():
    """Test getting student name"""
    student = Student("Bob", 92)
    assert student.get_name() == "Bob"

def test_student_get_grade():
    """Test getting student grade"""
    student = Student("Charlie", 78)
    assert student.get_grade() == 78

def test_student_set_grade():
    """Test updating student grade"""
    student = Student("David", 80)
    student.set_grade(90)
    assert student.get_grade() == 90

def test_student_different_grades():
    """Test students with different grades"""
    student1 = Student("Eve", 95)
    student2 = Student("Frank", 67)
    
    assert student1.get_name() == "Eve"
    assert student1.get_grade() == 95
    assert student2.get_name() == "Frank"
    assert student2.get_grade() == 67

def test_student_grade_update():
    """Test multiple grade updates"""
    student = Student("Grace", 70)
    student.set_grade(75)
    assert student.get_grade() == 75
    student.set_grade(80)
    assert student.get_grade() == 80

def test_student_string_name():
    """Test student with string name"""
    student = Student("Henry", 88)
    assert student.get_name() == "Henry"
    assert isinstance(student.get_name(), str)

def test_student_numeric_grade():
    """Test student with numeric grade"""
    student = Student("Ivy", 93)
    assert student.get_grade() == 93
    assert isinstance(student.get_grade(), int)
