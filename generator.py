def my_generator(n):
    value = 0
    while value < n:
        yield value
        value = value + 5


print(my_generator(50))

for v in my_generator(50):
    print(v)


def sq(n):
    for i in range(n):
        yield i * i


for j in sq(70):
    print(j)
