class Lion:
    def __init__(self, name):
        self.name = name


class Zoo:
    def __init__(self):
        self.lions = []

    def add_lion(self, lion_name):
        new_lion = Lion(lion_name)
        self.lions.append(new_lion)

    def remove_lion(self, lion_name):
        index = -1
        for i in range(len(self.lions)):
            if self.lions[i].name == lion_name:
                index = i
        if index == -1:
            raise Exception("The lion {} is not found ".format(lion_name))
        self.lions.remove(self.lions[index])

    def get_lion_amount(self):
        return len(self.lions)


zoo = Zoo()
print('Lion amount in initialization : {} '.format(zoo.get_lion_amount()))
zoo.add_lion('Ethan')
zoo.add_lion('Woho')

print('Lion amount in the middle of adding : {} '.format(zoo.get_lion_amount()))
zoo.add_lion('Bla')
zoo.add_lion('Bidibido')
print('Lion amount after adding all lions : {} '.format(zoo.get_lion_amount()))
zoo.remove_lion('Bla')
print('Lion amount in the after remove of Bla : {} '.format(zoo.get_lion_amount()))
