# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three-digit number: "))

d1 = num // 100        # Hundreds place
d2 = (num // 10) % 10  # Tens place
d3 = num % 10          # Units place

rev = (d3 * 100) + (d2 * 10) + d1

if num == rev:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is NOT a Palindrome number.")
