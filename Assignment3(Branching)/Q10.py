# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

Gender = input('Enter Gender (M/F) : ')
print(Gender)

Age = int(input('Enter Age : '))

if(Gender == 'F'):
    if(Age >= 18):
        print('Elibgible for marriage')
    else:
        print('Elibgible for marriage')    
else:
    if(Age >= 21):
        print('Elibgible for marriage')
    else:
        print('Elibgible for marriage')  