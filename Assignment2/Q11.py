# 11. Write a program to accept an integer amount from user and tell minimum
    #number of notes needed for representing that amount.

amount = int(input('Enter amount:'))

# Max Note = 2000

d1 = amount // 2000
amount = amount % 2000
print(d1)
print(amount)

# 2nd Max Note 500
d2 = amount // 500
amount = amount % 500

print(d2)
print(amount)

print(f'For given amount we need min  notes are {d1 + d2}')