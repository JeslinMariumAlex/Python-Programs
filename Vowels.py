st=input("Enter the String: ")
vowels="aeiouAEIOU"
c=0
for i in st:
	if i in vowels:
		c=c+1
print(c)