n = int(input("Enter the lines:"))
for k in range(n, 0, -1):
    for i in range(1, k + 1):
        for j in range(n, 0, -1):
            if j > i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        for j in range(1, i):
            print("*", end=" ")
        print()
