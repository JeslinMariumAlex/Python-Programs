n=int(input("Enter the Number of lines:"))
for i in range(1,n+1):
	for j in range(1,n+1):
		if j>=i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
for i in range(1,n+1):
	for j in range(n,0,-1):
		if j>i:
			print(" ",end=" ")
		else:
			print("*",end=" ")
	print()
		