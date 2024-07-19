n = int(input("Enter the Number of lines:"))
for k in range(n, 0, -1):
    for i in range(1, k+1):
        for j in range(1, i + 1):
            print(j, end=" ")

        print()
    for i in range(k-1, 1, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
print(k)
