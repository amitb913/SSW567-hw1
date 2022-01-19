# Amit Bhatnagar
# Using pytest to unit test classify_triangle(a, b, c)
def classify_triangle(a, b, c):
    def get_triangle_type():
        triangle_type = "Scalene"
        if a == b and b == c:
            triangle_type = "Equilateral"
        elif a == b or b == c or a == c:
            triangle_type = "Isosceles"
        return triangle_type

    def is_right():
        sides = [a, b, c]
        maxSide = max(sides)
        sides.remove(maxSide)
        if((sides[0]**2 + sides[1]**2)**0.5 == maxSide):
            return True
        return False

    return get_triangle_type(), is_right()


def test_classify_triangle():
    # Result is given as (triangle_type, is_right)
    # where triangle_type can be 'Equilateral', 'Isosceles', or 'Scalene'
    # and is_right can be True or False

    assert classify_triangle(3, 3, 3) == ('Equilateral', False)
    assert classify_triangle(4, 4, 4) == ('Equilateral', False)
    assert classify_triangle(10, 10, 10) == ('Equilateral', False)
    assert classify_triangle(1, 1, 2**0.5) == ('Isosceles', True)
    assert classify_triangle(3, 3, 4) == ('Isosceles', False)
    assert classify_triangle(3, 4, 5) == ('Scalene', True)
    assert classify_triangle(5, 12, 13) == ('Scalene', True)
    assert classify_triangle(1, 4, 7) == ('Scalene', False)
    assert classify_triangle(6, 9, 3) == ('Scalene', False)


print("classify_triangle(3, 3, 3)):", classify_triangle(3, 3, 3))
print("classify_triangle(4, 4, 4)):", classify_triangle(4, 4, 4))
print("classify_triangle(10, 10, 10)):", classify_triangle(10, 10, 10))
print("classify_triangle(1, 1, 2**0.5)):", classify_triangle(1, 1, 2**0.5))
print("classify_triangle(3, 3, 4)):", classify_triangle(3, 3, 4))
print("classify_triangle(3, 4, 5)):", classify_triangle(3, 4, 5))
print("classify_triangle(5, 12, 13)):", classify_triangle(5, 12, 13))
print("classify_triangle(1, 4, 7)):", classify_triangle(1, 4, 7))
print("classify_triangle(6, 9, 3)):", classify_triangle(6, 9, 3))

test_classify_triangle()

# use python3 hw1.py to run the function itself
# use pytest hw1.py to run the test