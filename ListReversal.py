n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
lst = []
for i in range(0, n):
    k = int(input())
    lst.append(k)
print("List before reverse:", lst)
for i in range(0, n // 2):
    temp = lst[i]
    lst[i] = lst[n - i - 1]
    lst[n - i - 1] = temp
print("List after reverse:", lst)

