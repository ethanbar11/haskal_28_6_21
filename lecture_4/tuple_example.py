import random

# lst = [1, 2, 3, 4]
# lst.append(5)
# lst[0] = 5
# print(lst)
#
# tup = (1, 2, 3)
# print(tup[0])
# print(tup)
#
# lst = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]
# print(lst.count(1))
#
# lst2 = lst

lst = []
for i in range(100):
    lst.append(random.randint(1, 100))
print(lst)
lst.sort(reverse=True)
print(lst)
if 1 in lst:
    print('1 is in the list!')
else:
    print('1 is not int the list!')