# 10. Write a program to reverse three-digit number.

num = int(input("Enter a three-digit number: "))

d1 = num // 100        # Hundreds place
d2 = (num // 10) % 10  # Tens place
d3 = num % 10          # Units place

rev = (d3 * 100) + (d2 * 10) + d1

print(f"Reverse of {num} = {rev}")