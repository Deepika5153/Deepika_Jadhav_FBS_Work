# 5. Write a program to enter P, T, R and calculate Compound Interest.

PrincipalAmount = int(input('Enter principal Amount : '))
ROI = int(input('Enter Rate of Interest : '))
Time = int(input('Enter Time period : '))


amount = PrincipalAmount * (1 + ROI/100) ** Time
print(amount)
compoundIntrest =  amount - PrincipalAmount

print(f'Compound Intrest is :  {compoundIntrest}')



