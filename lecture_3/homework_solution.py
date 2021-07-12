# PracticePython, Lists less than 10
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('The length of a is:', len(a))
for i in range(len(a)):
    if a[i] < 5:
        # print('a[', i, ']:', a[i])
        print('a in index {} is equal to {}'.format(i, a[i]))
