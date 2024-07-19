s1 = set()
even = []
odd = []
n = int(input("Enter the number of elements:"))
print("Enter the Elements:")
for i in range(0, n):
    k = int(input())
    s1.add(k)
print("Set elements are:", s1)
for i in s1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("List of Even numbers:", even)
print("List of Odd numbers:", odd)
