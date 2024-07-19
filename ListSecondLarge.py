n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
lst = []
big = 0
s_big = 0
for i in range(0, n):
    k = int(input())
    lst.append(k)
for i in range(0, n):
    if lst[i] > big:
        big = lst[i]
print("Largest number:", big)
for i in range(0, n):
    if lst[i] > s_big and lst[i] != big:
        s_big = lst[i]
print("Second Largest number:", s_big)
