areaOfWall = int(input('Enter Area of 1 Wall : '))
Interiorcost = int(input('Enter cose of Interior Wall painting : '))
Exteriorcost = int(input('Enter cose of Exterior Wall painting : '))

Interior_Area = areaOfWall * 8
Interior_cost = Interior_Area * Interiorcost
print(f'Cost of Paiting Interior Wall of Given diagram is {Interior_cost}')

Exterior_Area = areaOfWall * 7
Exterior_cost = Exterior_Area * Exteriorcost
print(f'Cost of Paiting Exterior Wall of Given diagram is {Exterior_cost}')

Total_cost = Interior_cost + Exterior_cost
print(f'Total Cost of Paiting of Given diagram is {Total_cost}')