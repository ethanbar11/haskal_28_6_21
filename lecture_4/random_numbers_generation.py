from random import randint


def create_random_list(amount, bottom, top):
    lst = []
    for i in range(amount):
        lst.append(randint(bottom, top))
    return lst

print(create_random_list(50,20,35))