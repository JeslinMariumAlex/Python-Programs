n=int(input("Enter the Number of lines:"))
for i in range(n,0,-1):
	for j in range(1,i+1):
		print(j*2,end=" ")
	print()