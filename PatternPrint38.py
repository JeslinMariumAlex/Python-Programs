n = int(input("Enter the Number of lines:"))
for i in range(1, n):
    for j in range(1, n + 1):
        if i > j:
            print(" ", end=" ")
        else:
            print(i, end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if i <= j:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
