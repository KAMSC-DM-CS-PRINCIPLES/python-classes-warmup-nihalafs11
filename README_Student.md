# Student Class Assignment

## Overview
Create a `Student` class that stores and manages student information including name and grade.

## Requirements

### Class Structure
Your `Student` class should have the following methods:

1. **`__init__()`**
   - Initialize a student with a name and grade
   - Store both name and grade as instance variables

2. **`get_name()`**
   - Return the student's name

3. **`get_grade()`**
   - Return the student's grade

4. **`set_grade()`**
   - Update the student's grade to the new value
   - Modify the instance variable directly

## Expected Behavior

### Example Usage
```python
# Create a student
student = Student("Alice", 85)
print(student.get_name())   # Should output: "Alice"
print(student.get_grade())  # Should output: 85

# Update the grade
student.set_grade(90)
print(student.get_grade())  # Should output: 90

# Access attributes directly
print(student.name)   # Should output: "Alice"
print(student.grade)  # Should output: 90

# Create multiple students
student1 = Student("Bob", 92)
student2 = Student("Charlie", 78)

print(student1.get_name())   # Should output: "Bob"
print(student2.get_grade())  # Should output: 78
```

### Test Cases
Your implementation should pass all the following test cases:

1. **Student creation**: Create student with name and grade, verify both are stored correctly
2. **Get name**: Method returns the correct student name
3. **Get grade**: Method returns the correct student grade
4. **Set grade**: Method updates the grade and both direct access and getter return new value
5. **Different grades**: Multiple students can have different grades
6. **Grade updates**: Multiple grade updates work correctly
7. **String name**: Student name is stored as a string
8. **Numeric grade**: Student grade is stored as a number

## Implementation Tips

- Store both name and grade as instance variables
- The `set_grade()` method should modify the instance variable directly
- Both getter methods should return the stored values
- Make sure your class follows the exact method signatures shown above
- The class should be simple and straightforward - no complex validation needed

## Data Types
- **Name**: Should be a string
- **Grade**: Should be a number (int or float)

