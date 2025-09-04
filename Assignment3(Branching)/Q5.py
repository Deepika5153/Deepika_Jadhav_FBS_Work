# 5. Write s1 program to check whether the triangle is equilateral, isosceles or scalene triangle.

s1 = float(input("Enter first side: "))
s2 = float(input("Enter second side: "))
s3 = float(input("Enter third side: "))

if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    
    if s1 == s2 == s3:
        print("The triangle is Equilateral.")   # All sides equal
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("The triangle is Isosceles.")     # Any two sides equal
    else:
        print("The triangle is Scalene.")       # All sides different

else:
    print("The given sides do not form a valid triangle.")