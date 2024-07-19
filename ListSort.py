n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
a = []
temp = 0
for i in range(0, n):
    k = int(input())
    a.append(k)
for i in range(0, n):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
print("Sorted List ")
for i in range(0, n):
    print(a[i])
