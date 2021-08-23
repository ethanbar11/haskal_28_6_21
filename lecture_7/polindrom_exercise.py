def is_polindrom(s):
    s_without_spaces = s.replace(' ', '')
    return s_without_spaces[::-1] == s_without_spaces


lst = ['HelleH', 'Hel leH', 'Bla']
for word in lst:
    print('The word {} is polindrom {}'.format(word, is_polindrom(word)))
