# Amit Bhatnagar
# Using pytest to unit test classify_triangle(a, b, c)

#replaced some variables/functions with more meaningful names
def classify_triangle(side1, side2, side3):
    def get_triangle_type():
        triangle_type = "Scalene"
        if side1 == side2 and side2 == side3:
            triangle_type = "Equilateral"
        elif side1 == side2 or side2 == side3 or side1 == side3:
            triangle_type = "Isosceles"
        return triangle_type

    def is_right_triangle():
        sides = [side1, side2, side3]
        maxSide = max(sides)
        sides.remove(maxSide)
        if((sides[0]**2 + sides[1]**2)**0.5 == maxSide):
            return True
        return False

    return get_triangle_type(), is_right_triangle()


def test_classify_triangle():
    # Result is given as (triangle_type, is_right_triangle)
    # where triangle_type can be 'Equilateral', 'Isosceles', or 'Scalene'
    # and is_right_triangle can be True or False
    
    #put tests in try except block to catch errors
    
    try:
        assert classify_triangle(3, 3, 3) == ('Equilateral', False)
    except AssertionError:
        print("Test 1 failed")
    try:
        assert classify_triangle(4, 4, 4) == ('Equilateral', False)
    except AssertionError:
        print("Test 2 failed")
    try:
        assert classify_triangle(10, 10, 10) == ('Equilateral', False)
    except AssertionError:
        print("Test 3 failed")
    try:
        assert classify_triangle(1, 1, 2**0.5) == ('Isosceles', True)
    except AssertionError:
        print("Test 4 failed")
    try:
        assert classify_triangle(3, 3, 4) == ('Isosceles', False)
    except AssertionError:
        print("Test 5 failed")
    try:
        assert classify_triangle(3, 4, 5) == ('Scalene', True)
    except AssertionError:
        print("Test 6 failed")
    try:
        assert classify_triangle(5, 12, 13) == ('Scalene', True)
    except AssertionError:
        print("Test 7 failed")
    try:
        assert classify_triangle(1, 4, 7) == ('Scalene', False)
    except AssertionError:
        print("Test 8 failed")
    try:
        assert classify_triangle(6, 9, 3) == ('Scalene', False)
    except AssertionError:
        print("Test 9 failed")



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