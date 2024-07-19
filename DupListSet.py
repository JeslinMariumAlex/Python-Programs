lst = []
n = int(input("Enter the number of elements:"))
print("Enter the Elements:")
for i in range(0, n):
    k = int(input())
    lst.append(k)
print("List elements are:", lst)
s = set(lst)
print("Set elements are:", s)
