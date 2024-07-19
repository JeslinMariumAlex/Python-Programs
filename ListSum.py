lst = []
n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
for i in range(0, n):
    k = int(input())
    lst.append(k)
print("Sum of elements")
s = 0
for i in range(0, n):
    s = s + lst[i]
print(s)
