# Expecting an input in form of:
# D\W Number, D\W Number, D\W number .....
user_line = 'D 100, W 200, D 450, D 600'
user_operations = [100, -200, 450, 600]


def decode_commands(line):
    commands = line.split(',')
    operations = []
    for i in range(len(commands)):
        command = commands[i]  # command = 'D 100'
        values = command.split(' ')  # values=['D','100']
        if values[0] == 'D':
            operations.append(int(values[1]))
        elif values[0] == 'W':
            operations.append(-int(values[1]))
        else:
            print('The operation {} is not recognized'.format(values[0]))
            # This is a problem, because the operations requested is not recognized.
            pass
    return operations


# This is going to return the money in the account after all the operations.
def calculate_account_money(line):
    operations = decode_commands(line)
    s = 0
    for i in range(len(operations)):
        s += operations[i]
    return s


line = input('Please enter a line of commands: ')
money = calculate_account_money(line)
print('The money in the account is : {}  '.format(money))
