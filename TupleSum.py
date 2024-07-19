a = ()
s = 0
n = int(input("Enter the number of elements:"))
print("Enter the tuple elements:")
for i in range(0, n):
    no = int(input())
    a = a + (no,)
print("Elements are:", a)
for i in range(0, n):
    s = s + a[i]
print("Sum is:", s)
