n=int(input("Enter the Number of lines:"))
for i in range(n,1,-1):
	for j in range(n,i-1,-1):
		print(j,end=" ")
	print()
for i in range(1,n+1):
	for j in range(n,i-1,-1):
		print(j,end=" ")
	print()