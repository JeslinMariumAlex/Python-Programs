lst = []
n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
for i in range(0, n):
    k = int(input())
    lst.append(k)
print(lst)
print("................")
for i in range(0, n):
    print(lst[i])
print("................")
for i in lst:
    print(i)

