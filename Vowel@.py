st = input("Enter the String: ")
vowels = "aeiouAEIOU"
new_str = " "
for i in st:
    if i in vowels:
        new_str = new_str + "*"
    else:
        new_str = new_str + i
print("Original String:", st)
print("New String:", new_str)
