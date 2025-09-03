# 7. Program to Find the Roots of a Quadratic Equation

a = float(input('Enter coefficient a for quadratic Equation : '))
b = float(input('Enter coefficient b for quadratic Equation : '))
c = float(input('Enter coefficient c for quadratic Equation : '))

r =  ((b ** 2) -(4 * a * c)) ** 0.5

root1 = (-b + r ) / (2 * a)
root2 = (-b - r) / (2 * a)

print(f'root1 of qudratic equation is - {root1}')
print(f'root2 of qudratic equation is - {root2}')

