n = int(input("Enter the Number of lines:"))
for i in range(1, 2*n):
    for k in range(1, n + 1):
        for j in range(1, 2*n):
            if j == i or i+j == 2*n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
