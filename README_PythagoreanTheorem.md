# PythagoreanTheorem Class Assignment

## Overview
Create a `PythagoreanTheorem` class that calculates the hypotenuse of a right triangle using the Pythagorean theorem: a² + b² = c²

## Requirements

### Class Structure
Your `PythagoreanTheorem` class should have the following methods:

1. **`__init__()`**
   - Initialize a triangle with given side lengths a and b
   - Store both side lengths as instance variables

2. **`hypotenuse()`**
   - Calculate the hypotenuse using the Pythagorean theorem
   - Formula: c = √(a² + b²)
   - Return the length of the third side (hypotenuse)
   - Use `math.sqrt()` for the square root calculation


## Expected Behavior

### Example Usage
```python
import math

# Create triangle with sides 3 and 4
triangle = PythagoreanTheorem(3, 4)
print(triangle.hypotenuse())  # Should output: 5.0


# Create triangle with sides 5 and 12
triangle2 = PythagoreanTheorem(5, 12)
print(triangle2.hypotenuse())  # Should output: 13.0

# Create triangle with equal sides
triangle3 = PythagoreanTheorem(1, 1)
print(triangle3.hypotenuse())  # Should output: 1.4142135623730951 (√2)
```

### Test Cases
Your implementation should pass all the following test cases:

1. **3-4-5 triangle**: Classic right triangle
2. **5-12-13 triangle**: Another classic right triangle
3. **1-1 triangle**: Equal sides
4. **6-8-10 triangle**: Another common right triangle
5. **7-24-25 triangle**: Larger right triangle
6. **9-12-15 triangle**: Another right triangle
7. **Decimal sides**: Works with decimal side lengths

## Implementation Tips

- Import the `math` module at the top of your file
- Use `math.sqrt()` for square root calculations
- Store side lengths as instance variables
- The hypotenuse method should return a float value
- Test your calculations with known right triangles to verify accuracy

## Mathematical Background
The Pythagorean theorem states that in a right triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides:

- a² + b² = c²
- Where c is the hypotenuse, and a and b are the other two sides

