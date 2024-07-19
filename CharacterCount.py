st=input("Enter the String: ")
ch=input("Enter the Character to be searched:")
count=0
for x in st:
	if x==ch:
		count+=1
print("Number of times",ch,"occurs is",count)