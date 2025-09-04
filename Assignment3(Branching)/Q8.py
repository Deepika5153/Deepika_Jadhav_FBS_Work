#8. Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)
import random
Default_UI = 'Deepika5153'
Default_PW = 'Deepika@5153'

User_name = input('Enter Username : ')
User_PW = input('Enter Password : ')

if(Default_UI == User_name and Default_PW == User_PW):
    print('Entered username and password is correct')
    captcha = random.randint(11111,99999)
    print(f'Captcha is - {captcha}')
    User_Captcha = int(input ('Reenter the above Captcha : '))

    if(captcha == User_Captcha):
        print('Successful')
    else:
        print('UnSuccessful')
else:
    print('Entered username and password is not correct')




   

