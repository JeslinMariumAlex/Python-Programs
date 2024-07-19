num1 = (1, 2, 3, 4, 5)
num2 = (11, 12, 13, 14, 15)

res = map(lambda n1, n2: n1 + n2, num1, num2)
print(res)
for i in res:
    print(i)
