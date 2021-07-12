# Exercise 1
x = 0
while x <= 1000:
    print(x)
    x += 2

# Exercise 2
x = int(input('Please enter an odd number between 100 and 350:'))
if x % 2 == 1 and x>=100 and x<=350:
    print('Woho!')

# Exercise 3
bottom = int(input('Enter the lower bound: '))
top = int(input('Enter the upper bound: '))
if top < bottom:
    print('Very bad!')
else:
    x = bottom
    while x <= top:
        print(x)
        x += 1
