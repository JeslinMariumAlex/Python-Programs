n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
a = []
for i in range(0, n):
    k = int(input())
    a.append(k)
element = int(input("Enter the element to be deleted:"))
index = int(input("Enter the index value:"))
for i in range(index, n - 1):
    a[i] = a[i + 1]
n = n - 1
print("List elements are:")
for i in range(0, n):
    print(a[i])
