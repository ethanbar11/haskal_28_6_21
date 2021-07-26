def get_number():
    is_valid = False
    x = -1
    while not is_valid:
        try:
            x = int(input('Please enter a number between 0-10000'))
            if 0 <= x <= 10000:
                is_valid = True
        except Exception as e:
            pass
    return x

print('The number you entered is : {}'.format(get_number()))