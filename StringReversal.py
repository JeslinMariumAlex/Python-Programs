# String reversal using slicing
# st = input("Enter the String: ")
# for i in st[::-1]:
#    print(i, end='')

# String reversal without using slicing

word = input("Enter the Word: ")
k = len(word)
rev = " "
for i in range(0, k):
    rev = rev + word[k - i - 1]
print(rev)
