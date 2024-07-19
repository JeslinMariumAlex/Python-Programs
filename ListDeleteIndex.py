n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
a = []
for i in range(0, n):
    k = int(input())
    a.append(k)
index = int(input("Enter the index value:"))
dn = int(input("Enter the number of elements to be deleted:"))
for i in range(index + dn, n):
    a[i - dn] = a[i]
n = n - dn
print("List elements are:")
for i in range(0, n):
    print(a[i])
