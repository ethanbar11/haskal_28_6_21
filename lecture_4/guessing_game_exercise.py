from random import randint

bottom = int(input('Please enter the lower bound of guessing: '))
upper = int(input('Please enter the upper bound of guessing: '))
target = randint(bottom, upper)
is_finished = False

while not is_finished:
    guess = int(input('Please enter a guess: '))
    if guess == target:
        print('Very good! this was our guess!')
        is_finished = True
    else:
        print('Very shameful. Try again!')

print('The game is finished.')
