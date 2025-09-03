# 4. Write a program to enter P, T, R and calculate simple Interest.

PrincipalAmount = int(input('Enter principal Amount : '))
ROI = int(input('Enter Rate of Interest : '))
Time = int(input('Enter Time period : '))

SI = PrincipalAmount * ROI * Time / 100
print(f'Simple Interest is {SI}')