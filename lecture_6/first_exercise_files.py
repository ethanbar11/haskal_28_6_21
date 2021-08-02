original_name = input('Please enter file name to copy: ')
with open(original_name, 'r') as original_file:
    original_lines = original_file.readlines()
    new_name = 'my_new_file.txt'
    with open(new_name, 'w') as new_file:
        new_file.writelines(original_lines)
