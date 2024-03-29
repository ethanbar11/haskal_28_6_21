class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        return self.lst.pop()

    def top(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        return self.lst[-1]

    def __add__(self, other):
        new_lst = self.lst + other.lst
        new_stack = Stack()
        new_stack.lst = new_lst

    def __eq__(self, other):
        if len(self.lst) != len(other.lst):
            return False
        for i in range(len(self.lst)):
            if self.lst[i] != other.lst[i]:
                return False
        return True


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.top())
print(stack.pop())
