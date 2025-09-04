# 7. Find the sum of three-digit number.

num = int(input("Enter a 3 Digit Number :"))

d1 = num % 10
num = num // 10
print(d1)
print(num)

d2 = num % 10
num = num // 10
print(d2)
print(num)

d3 = num % 10
num = num // 10
print(d3)
print(num)

print(f'd1:{d1}, d2:{d2},d3:{d3}')
print(f'Sum of given 3 digit nymber is {d1 + d2 + d3}')