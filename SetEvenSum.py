s1 = set()
n = int(input("Enter the number of elements:"))
print("Enter the Elements:")
for i in range(0, n):
    k = int(input())
    s1.add(k)
print("Set elements are:", s1)
s_even = 0
s_odd = 0
for i in s1:
    if i % 2 == 0:
        s_even = s_even + i
    else:
        s_odd = s_odd + i
print("Sum of Even numbers:", s_even)
print("Sum of Odd numbers:", s_odd)
