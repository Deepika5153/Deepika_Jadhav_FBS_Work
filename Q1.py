# 1. Write a program to calculate the percentage of student based on marks of any 5
#    subjects.

m1 = int(input('Enter Marks of Subject 1:'))
m2 = int(input('Enter Marks of Subject 2:'))
m3 = int(input('Enter Marks of Subject 3:'))
m4 = int(input('Enter Marks of Subject 4:'))
m5 = int(input('Enter Marks of Subject 5:'))

gained_marks = m1 + m2 + m3 + m4 + m5

Perctange = (gained_marks /500) * 100
print(f'Perctange is {Perctange}%')