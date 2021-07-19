def reverse_sentence(s):
    words = s.split(' ')
    words.reverse()
    # This returns the words list after we reversed.
    new_s = ''
    for i in range(len(words)):
        new_s += words[i]+' '
    print(new_s)
    print(words)
    return new_s


s = 'Hello my world!'
print('Before', s)
print('After', reverse_sentence(s))
