s1 = set()
s2 = set()
n = int(input("Enter the number of elements:"))
print("Enter the Elements:")
for i in range(0, n):
    k = int(input())
    s1.add(k)
print("Set elements are:", s1)
for i in s1:
    if i != 0 and i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            s2.add(i)
print("Prime numbers in the Set:", s2)
lst = list(s2)
print("Prime numbers in the List:", lst)
