# 1. Write a program to check if the given number is positive or negative.

num = int(input('Enter Number :'))

if(num > 0):
    print(f'Given number {num} is Positive')
elif(num < 0):
    print(f'Given number {num} is Negative') 
else:
    print(f'Given number {num} is Nutral')      