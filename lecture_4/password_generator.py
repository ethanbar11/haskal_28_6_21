import string

# THIS IS THE GOOD WAY
from random import randint
import random


# THIS IS BAD
# from random import *

def create_password(length):
    password = ''
    types = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    for i in range(length):
        # Gives me a random number between 0 and 3
        t = randint(0, len(types) - 1)
        # This is the random string im going to take letter from
        s = types[t]
        # This is going the index of the random letter I'm going to choose from s
        letter_index = randint(0, len(s) - 1)
        letter = s[letter_index]
        password += letter
    return password


print(create_password(10))
