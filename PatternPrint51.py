n = int(input("Enter the Number of lines:"))
for i in range(1,n ):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(i, end=" ")
    for k in range(0, i + 1):
        print(k, end=" ")
    print()