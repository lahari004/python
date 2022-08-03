import cmath
class CIRCLE:
    r = int(input("radius : "))
    area = cmath.pi*r*r
    perimeter = 2*cmath.pi*r
    print("Area of circle : ", area)
    print("Perimeter of circle : ", perimeter)
