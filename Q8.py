# 8. Write a program to convert days into years, weeks and days.

totaldays = int(input('Enter total days : '))
years = totaldays // 365
print(f'years = {years}')
totaldays = totaldays % 365
months = totaldays // 7
print(f'months = {months}')
totaldays = totaldays % 7
print(f'days = {totaldays}')
