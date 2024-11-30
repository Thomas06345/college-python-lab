'''Author:Thomas Cherian
   date: 30-11-24
   python program:To check is the sides of a triangle are part of a right angle triangle.'''
def is_right_angle_trinagle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        return True
    return False

side1=int(input("Enter side1 of the triangle:"))
side2=int(input("Enter side2 of the triangle:"))
side3=int(input("Enter side3 of the triangle:"))
if is_right_angle_trinagle(side1,side2,side3):
    print(f"The gives sides are part of a right angle triangle")
else:
    print(f"The gives sides are not part of a right angle triangle")