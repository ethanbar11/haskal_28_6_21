amount = int(input('Please enter the amount of Fibonacci numbers: '))
first = 1
second = 1
print(first)
print(second)
for i in range(amount - 2):
    current = first + second
    print(current)
    first = second
    second = current
