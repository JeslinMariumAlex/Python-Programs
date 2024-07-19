n = int(input("Enter the number of elements in the list:"))
print("Enter the elements:")
lst = []
s_even = 0
s_odd = 0
for i in range(0, n):
    k = int(input())
    lst.append(k)
for i in lst:
    if i % 2 == 0:
        s_even = s_even + i
    else:
        s_odd = s_odd + i
print("Sum of Even numbers:", s_even)
print("Sum of Odd numbers:", s_odd)
