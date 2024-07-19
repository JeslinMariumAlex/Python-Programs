n = int(input("Enter the lines:"))
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    for k in range(1, i):
        print("*", end=" ")
    print()
