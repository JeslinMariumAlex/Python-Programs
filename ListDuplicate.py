n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
a = []
not_duplicate = []
for i in range(0, n):
    k = int(input())
    a.append(k)
for element in a:
    if element not in not_duplicate:
        not_duplicate.append(element)
print(not_duplicate)
