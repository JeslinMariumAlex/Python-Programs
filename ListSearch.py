n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
lst = []
for i in range(0, n):
    k = int(input())
    lst.append(k)
a = int(input("Enter the element to be searched:"))
if a in lst:
    print("Element found ")
else:
    print("Element not found")
