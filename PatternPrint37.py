n = int(input("Enter the Number of lines:"))
for i in range(n, 1, -1):
    for j in range(1, n + 1):
        if i <= j:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i > j:
            print(" ", end=" ")
        else:
            print(j, end=" ")
    print()
