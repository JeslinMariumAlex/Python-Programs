n = int(input("Enter the Number of lines:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i or j == (n+1)-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

