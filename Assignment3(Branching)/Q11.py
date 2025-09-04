# 11. Accept age of five people and also per person ticket amount and then calculate total
    # amount to ticket to travel for all of them based on following condition :
    # a. Children below 12 = 30% discount
    # b. Senior citizen (above 59) = 50% discount
    # c. Others need to pay full.

ticket_price = float(input("Enter ticket price per person: "))
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))

if age1 < 12:
    p1 = ticket_price - ticket_price * (30/100)
elif age1 > 59:
    p1 = ticket_price - ticket_price * (50/100)
else:
    p1 = ticket_price

if age2 < 12:
    p2 = ticket_price - ticket_price * (30/100)
elif age2 > 59:
    p2 = ticket_price - ticket_price * (50/100)
else:
    p2 = ticket_price

if age3 < 12:
    p3 = ticket_price - ticket_price * (30/100)
elif age3 > 59:
    p3 = ticket_price - ticket_price * (50/100)
else:
    p3 = ticket_price

if age4 < 12:
    p4 = ticket_price - ticket_price * (30/100)
elif age4 > 59:
    p4 = ticket_price - ticket_price * (50/100)
else:
    p4 = ticket_price  

if age5 < 12:
    p5 = ticket_price - ticket_price * (30/100)
elif age5 > 59:
    p5 = ticket_price - ticket_price * (50/100)
else:
    p5 = ticket_price      

print(f'Total ticket amount is : {p1 + p2 + p3 + p4 + p5}')