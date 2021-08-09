class Human:
    def __init__(self, name, id, birth_date):
        self.my_name = name
        self.my_id = id
        self.human_birth = birth_date

    def eat(self, food_amount):
        print('I ate {} wow, and my name is : {}'.format(food_amount, self.my_name))


class Office:
    def __init__(self):
        self.employees = {}

    def add_employee(self, human):
        self.employees[human.id] = human


ethan = Human("Ethan", 1, "12.8.80")
noy = Human("Noy", 2, "3.5.1963")
ethan.eat(15)
noy.eat(30)
