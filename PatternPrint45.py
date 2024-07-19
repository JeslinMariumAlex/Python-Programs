n = int(input("Enter the Number of lines:"))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == (n + 1) / 2 or j == (n + 1) / 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
