n = int(input("Enter the Number of lines:"))
for i in range(1, n + 1):
    for j in range(n, 1, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(j, end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
