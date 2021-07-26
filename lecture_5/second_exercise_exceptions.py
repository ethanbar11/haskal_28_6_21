def change_string(number, line):
    small_letter_counter = 0
    upper_letter_counter = 0
    digit_counter = 0
    other_counter = 0
    for c in line:
        c_ascii = ord(c)
        if 65 <= c_ascii <= 90:
            upper_letter_counter += 1
        elif 97 <= c_ascii <= 122:
            small_letter_counter += 1
        elif 48 <= c_ascii <= 58:
            digit_counter += 1
        else:
            other_counter += 1
    print(
        'Small : {} Upper : {} Digit : {} Other : {} '.format(small_letter_counter,
                                                              upper_letter_counter,
                                                              digit_counter,
                                                              other_counter))
    if number == 1:
        return line.upper()
    elif number == 2:
        return line.lower()
    else:
        # Here comes exception.
        pass

line='Hello 3 My name is steve !!!!!!'
new_line=change_string(1,line)
print(new_line)