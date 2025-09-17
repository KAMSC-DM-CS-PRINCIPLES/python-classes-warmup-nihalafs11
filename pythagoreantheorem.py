import math

class PythagoreanTheorem:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def hypotenuse(self):
        return math.sqrt(self.side_a**2 + self.side_b**2)


if __name__ == "__main__":
    triangle = PythagoreanTheorem(3, 4)
    print(f"Triangle with sides 3 and 4:")
    print(f"Hypotenuse: {triangle.hypotenuse()}")
    
    triangle2 = PythagoreanTheorem(5, 12)
    print(f"Triangle with sides 5 and 12:")
    print(f"Hypotenuse: {triangle2.hypotenuse()}")
    
    triangle3 = PythagoreanTheorem(1, 1)
    print(f"Triangle with sides 1 and 1:")
    print(f"Hypotenuse: {triangle3.hypotenuse()}")