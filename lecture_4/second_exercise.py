def str_binary_to_decimal(s):
    num = 0
    for i in range(len(s)):
        letter = s[i]
        if letter == '1':
            num += pow(2, len(s) - i - 1)
    return num


s = input('Please enter comma-separated binary numbers.')
numbers_as_string = s.split(',')
numbers = []
for i in range(len(numbers_as_string)):
    number_s = numbers_as_string[i]
    number = str_binary_to_decimal(number_s)
    if number % 5 == 0:
        numbers.append(str_binary_to_decimal(number_s))

print(numbers)

# Show in next lecture how to finish it.
