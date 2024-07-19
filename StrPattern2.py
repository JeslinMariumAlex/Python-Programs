word = input("Enter the Word: ")
n = len(word)
for i in range(1, n + 1):
    m = 0
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(word[m], end=" ")
            m += 1
    m = m - 2
    for k in range(1, i):
        print(word[m], end=" ")
        m = m - 1
    print(" ")
