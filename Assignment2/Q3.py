# 3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter remaining inches: "))

total_inches = (feet * 12) + inches

centimeters = total_inches * 2.54

meters = int(centimeters // 100)
remaining_cm = centimeters % 100

print(f"{feet} ft {inches} in = {meters} m {remaining_cm:.2f} cm")