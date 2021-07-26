# Assembly, C (No exceptions) - Deciding on some value that represents error.
# For example, -1 is very common.
# def sum(a, b):
#     return a + b
#
#
# sum('Hello', 5)

try:
    x = 3 / 0
    foo1()
    foo2()
    foo3()

    print('I succeed in this division!')
except ZeroDivisionError as e:
    x = 10
except Exception as e:
    print('I catched some exception')
print('Hello!')
