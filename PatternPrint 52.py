n = int(input("Enter the Number of lines:"))
for i in range(1, n + 1):
    for k in range(n, 0, -1):
        if k >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(0, n + 1):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(1, n + 1):
    for k in range(n, 0, -1):
        if k >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(0, n + 1):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()