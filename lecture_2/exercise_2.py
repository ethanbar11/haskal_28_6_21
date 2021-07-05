age=int(input('Please enter your age '))
height=int(input('Please enter your height: '))
if age>=8 and age<=18 and height>=115:
    print('You are good!')
elif age>18 and height>100:
    print('Ahla Bahla')
else:
    print('You are not eligible for the ride.')