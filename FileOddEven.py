n = int(input("Enter the count:"))
f = open("number_file.txt", "w")
print("Enter the numbers:")
for i in range(0, n):
    no = input()
    f.write(no + "\n")
f.close()
f = open("number_file.txt", "r")
o = open("even_file.txt", "w")
e = open("odd_file.txt", "w")
for i in range(0, n):
    x = int(f.readline())
    if x % 2 == 0:
        o.write(str(x) + "\n")
    else:
        e.write(str(x) + "\n")
f.close()
o.close()
e.close()
