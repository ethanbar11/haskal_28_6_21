class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return 'Item name : {} and item price : {}'.format(self.__name, self.__price)

    def __add__(self, other):
        return Item(self.__name + other.__name, self.__price + other.__price)


item1 = Item('Item1', 15)
item2 = Item('Item2', 20)
print(item1 + item2)
