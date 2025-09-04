# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

# For a triangle, the sum of any two sides must be greater than the third side (triangle inequality theorem)

s1 = float(input('Enter first side : '))
s2 = float(input('Enter second side : '))
s3 = float(input('Enter third side : '))

if( (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2) ):
    print('Triangle is valid')
else:
    print('Triangle is not valid')    