n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
a = []
lst = []
for i in range(0, n):
    k = int(input())
    a.append(k)
for i in range(0, n):
    if a[i] != 0 and a[i] != 1:
        for j in range(2, a[i]):
            if a[i] % j == 0:
                break
        else:
            lst.append(a[i])
print("Prime numbers:", lst)
