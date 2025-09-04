# 7. Write a program to check if user has entered correct userid and password.

Default_UI = 'Deepika5153'
Default_PW = 'Deepika@5153'

User_name = input('Enter Username : ')
User_PW = input('Enter Password : ')

if(Default_UI == User_name and Default_PW == User_PW):
    print('Entered username and password is correct')
else:
    print('Entered username and password is not correct')
