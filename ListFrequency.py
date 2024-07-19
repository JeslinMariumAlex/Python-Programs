n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
flag = 0
lst = []
count = 0
for i in range(0, n):
    k = int(input())
    lst.append(k)
a = int(input("Enter the element to be searched:"))
for i in range(0, n):
    if lst[i] == a:
        flag = 1
        count = count + 1
if flag == 1:
    print("Element found", count, "times")
else:
    print("Element not found")
