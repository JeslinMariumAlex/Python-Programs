n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
lst = []
for i in range(0, n):
    k = int(input())
    lst.append(k)
print("Menu:\n1.Display\n2.Insert\n3.Delete\n4.Search\n5.Sort")
c = int(input("Enter your choice:"))
if c == 1:
    print("List elements are :", lst)
elif c == 2:
    lst.append(0)
    element = int(input("Enter the element to be inserted:"))
    index = int(input("Enter the index value:"))
    for i in range(n, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = element
    print("List elements are:", lst)
elif c == 3:
    element = int(input("Enter the element to be deleted:"))
    index = int(input("Enter the index value:"))
    for i in range(index, n - 1):
        lst[i] = lst[i + 1]
    n = n - 1
    print("List elements are:")
    for i in range(0, n):
        print(lst[i])
elif c == 4:
    a = int(input("Enter the element to be searched:"))
    if a in lst:
        print("Element found ")
    else:
        print("Element not found")
elif c == 5:
    for i in range(0, n):
        for j in range(0, n - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    print("Sorted List ", lst)
else:
    print("Invalid Choice")
