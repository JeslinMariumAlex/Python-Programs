lst = []
a = []
freq = {}
output = []
n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
for i in range(0, n):
    k = int(input())
    lst.append(k)
print(lst)
for i in lst:
    if i not in a:
        a.append(i)
        freq[i] = 1
    else:
        freq[i] += 1
print("Frequency of elements:", freq)
