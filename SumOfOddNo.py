n=int(input("Enter the limit:"))
s=0
i=1
while i<=n:
	if i%2!=0:
		s=s+i
	i=i+1
print("sum=",s)