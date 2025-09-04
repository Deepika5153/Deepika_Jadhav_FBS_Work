# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.
# Angles method: For a triangle, sum of three angles must be 180° and each angle must be greater than 0.

a1 = float(input('Enter 1st Angle of triangle : '))
a2 = float(input('Enter 2nd Angle of triangle : '))
a3 = float(input('Enter 3rd Angle of triangle : '))

if( (a1 > 0 and a2 > 0 and a3 > 0 ) and   a1 + a2 + a3 == 180):
    print(f'The triangle is valid')
else:
    print(f'The triangle is not valid')  