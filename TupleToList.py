a = ()
n = int(input("Enter the number of items in the list:"))
print("Enter the elements:")
for i in range(0, n):
    no = int(input())
    a = a + (no,)
print("Tuple elements are:", a)
lst = list(a)
for i in range(0, n):
    lst[i] = lst[i] ** 2
print("List elements are:", lst)
a = tuple(lst)
print("List changed to Tuple:", a)
