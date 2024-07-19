l=int(input("Enter the Lowerlimit:"))
u=int(input("Enter the Upperlimit:"))
for i in range(l,u+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
			print(i)