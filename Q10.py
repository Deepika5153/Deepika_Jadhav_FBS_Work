# 10. Write a program to calculate area of an equilateral triangle.

side = int(input("Enter the length of a side: "))

# Formula: (√3 / 4) * a², with √3 ≈ 1.732
area = (1.732 / 4) * (side ** 2)

print(f"The area of the equilateral triangle is:", {area})