n=int(input("Enter the lines:"))
for i in range(n,0,-1):
	for j in range(1,i+1):
		if(j%2!=0):
			print("*",end=" ")
		else:
			print("+",end=" ")
	print()