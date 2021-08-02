try_another_input = True
while try_another_input:
    action = int(input('input a number between 1 to 100: '))
    print(action)
    try:
        if action > 0 and action <= 100:
            print('QK!')
            try_another_input = False
    except Exception as e:
        print('wrong input')
