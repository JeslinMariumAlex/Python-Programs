n = int(input("Enter the number of elements:"))
print("Enter the elements:")
lst = []
flag = 0
for i in range(n):
    k = int(input())
    lst.append(k)
print("List elements are:", lst)
for i in range(0, n):
    for j in range(0, n-1):
        if lst[j] == lst[j + 1]:
            flag = 1
if flag == 0:
    print("Elements are Unique")
else:
    print("Elements are not unique")
