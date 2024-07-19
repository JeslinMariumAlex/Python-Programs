word = input("Enter the Word: ")
k = len(word)
rev = ""
for i in range(0, k):
    rev = rev + word[k - i - 1]
if rev == word:
    print("Palindrome")
else:
    print("Not Palindrome")

"""st = input("Enter the string:")
i = 0
j = len(st) - 1
flag = True
while i <= j:
    if st[i] != st[j]:
        flag = False
        break
    i = i + 1
    j = j - 1
if flag == True:
    print("The given string", st, "is a palindrome")
else:
    print("The given string", st, "is not palindrome")"""
