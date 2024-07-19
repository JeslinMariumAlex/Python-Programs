n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
a = []
for i in range(0, n):
    k = int(input())
    a.append(k)
a.append(0)
element = int(input("Enter the element to be inserted:"))
index = int(input("Enter the index value:"))
for i in range(n, index, -1):
    a[i] = a[i - 1]
a[index] = element
print("List elements are:")
for i in range(0, n + 1):
    print(a[i])
