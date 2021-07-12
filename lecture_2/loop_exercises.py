# Exercise 1
# for i in range(1500, 2701):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)

# Exercise 5
word = input('Please enter a word: ')
for i in range(len(word)):
    print(word[len(word) - i - 1], end='')
