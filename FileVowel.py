f = open("newfile", "w")
data = input("Enter the content in the file:")
f.write(data)
f.close()
f = open("newfile", "r")
a = f.read()
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
for x in a:
    if x in vowel:
        count += 1
print("No of vowels in ", a, "is", count)
f.close()
