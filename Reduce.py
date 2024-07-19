from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def sumoflist(a, b):
    return a + b


result = reduce(sumoflist, numbers)
print("first", result)

x = reduce(lambda a, b: a + b, [2, 1, 4, 9])
print("second", x)

x = reduce(lambda a, b: a * a, [2, 1, 4, 9])
print("third", x)
