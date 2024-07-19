n = int(input("Enter the Number of lines:"))
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if j == i or i + j == 2 * n or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
