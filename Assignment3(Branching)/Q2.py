# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

alpabet = input('Enter an alphabet : ')

if(alpabet  in('aeiouAEIOU')):
    print(f'Given aphabet {alpabet} is vowel')
else:
    print(f'Given aphabet {alpabet} is consonant')



