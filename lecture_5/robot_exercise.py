import math


def read_lines():
    should_work = True
    lines = []
    while should_work:
        line = input('Please enter a robot move: ')
        if line == '':
            should_work = False
        else:
            lines.append(line)
    return lines


def convert_lines_to_steps(lines):
    steps = []
    for line in lines:
        values = line.split(' ')
        direction = values[0]
        amount_of_steps = int(values[1])
        if direction == 'UP':
            steps.append((0, amount_of_steps))
        elif direction == 'DOWN':
            steps.append((0, -amount_of_steps))
        elif direction == 'RIGHT':
            steps.append((amount_of_steps, 0))
        elif direction == 'LEFT':
            steps.append((-amount_of_steps, 0))
        else:
            print('BAD Request : {}'.format(line))
    return steps


def convert_steps_to_distance(steps):
    x_distance = 0
    y_distance = 0
    for step in steps:
        x_distance += step[0]
        y_distance += step[1]
    return math.sqrt(x_distance ** 2 + y_distance ** 2)


lines = read_lines()
steps = convert_lines_to_steps(lines)
distance = convert_steps_to_distance(steps)
print('The distance is : {}'.format(distance))
