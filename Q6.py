# 6. Write a Program to input two angles from user and find third angle of the
#triangle.

# Third Angle=180∘−(Angle1+Angle2)

angle1 = int(input('Enter 1 angle of triangle : '))
angle2 = int(input('Enter 2 angle of triangle : '))

angle3 = 180 - (angle1 + angle2)
print(f'third angle of a triangle is {angle3}')
