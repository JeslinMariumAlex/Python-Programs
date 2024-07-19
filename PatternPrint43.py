n = int(input("Enter the Number of lines:"))
for i in range(1, n + 1):
    for j in range(1, n):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(n, i - 1, -1):
        print("*", end=" ")
    print()
