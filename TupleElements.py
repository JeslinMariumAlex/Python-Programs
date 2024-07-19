a = ()
n = int(input("Enter the number of elements:"))
print("Enter the tuple elements:")
for i in range(0, n):
    no = int(input())
    a = a + (no,)
print("Elements are:", a)
print("........................")
for i in range(0, n):
    print(a[i])
print("........................")
for i in a:
    print(i)
print("........................")
i = 0
while i < n:
    print(a[i])
    i = i + 1
