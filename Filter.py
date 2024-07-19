alph = ['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'i']


def fill_vow(alph):
    vow = ['a', 'e', 'i', 'o', 'u']
    if alph in vow:
        return True
    else:
        return False


res = filter(fill_vow, alph)
print(res)
print(tuple(res))

