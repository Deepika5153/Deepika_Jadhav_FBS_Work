# 9. Write a program to swap two numbers without using third variable.

x = 10
y = 20
print(f'Before swaping Value of x : {x} and y : {y}')
x = x + y
y = x - y
x = x - y

print(f'After swaping Value of x : {x} and y : {y}')    