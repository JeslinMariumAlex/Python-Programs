n = int(input("Enter the Number of lines:"))
for i in range(n, 0, -1):
    for j in range(1, n+1):
        if i <= j:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
