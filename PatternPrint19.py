n=int(input("Enter the Number of lines:"))
for i in range(1,n):
	for j in range(1,i+1):
		print(j,end=" ")
	print()
for i in range(n,0,-1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()