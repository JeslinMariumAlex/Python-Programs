n = int(input("Enter the number of elements in the list:"))
print("Enter the elements:")
lst = []
even = []
odd = []
for i in range(0, n):
    k = int(input())
    lst.append(k)
for i in range(0, n):
    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])
print("List of Even numbers:", even)
print("List of Odd numbers:", odd)
