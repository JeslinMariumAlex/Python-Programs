n = int(input("Enter the Number of lines:"))
for i in range(1, n + 1):
    k = i
    for j in range(1, i + 1):
        print(k, end=" ")
        k = k + (n - j)
    print()
