n = int(input("Enter the number of elements:"))
print("Enter the tuple elements:")
tup = ()
count = 0
for i in range(0, n):
    no = int(input())
    tup = tup + (no,)
print("Tuple elements are:", tup)
a = int(input("Enter the element to be searched:"))
for i in range(0, n):
    if tup[i] == a:
        flag = 1
        count = count + 1
if flag == 1:
    print("Element found", count, "times")
else:
    print("Element not found")
