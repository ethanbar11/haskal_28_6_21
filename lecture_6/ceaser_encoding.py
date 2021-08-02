import string

lower_case_letters = string.ascii_lowercase


# Can only accept small letter text
def encrypt(text, move_amount):
    encrypted_text = ''
    for s in text:
        if s in lower_case_letters:
            original_index = lower_case_letters.find(s)
            new_index = (original_index + move_amount) % len(lower_case_letters)
            encrypted_text += lower_case_letters[new_index]
        else:
            encrypted_text += s
    return encrypted_text


def encrypt_file(path, new_path, move_amount):
    with open(path, 'r') as original_file:
        text = original_file.read()
        encrypted_text = encrypt(text, move_amount)
        with open(new_path, 'w') as encrypted_file:
            encrypted_file.write(encrypted_text)
    print('hello')

option = input('Please enter if you want to encrypt (e) / decrypt (d) : ')
original_path = input('Please enter file name : ')
new_path = input('Please enter new file name : ')
if option == 'e':
    encrypt_file(original_path, new_path, 1)
elif option == 'd':
    encrypt_file(original_path, new_path, -1)
