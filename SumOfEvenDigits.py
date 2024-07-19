n=int(input("Enter the number:"))
s=0
while n!=0:
	d=n%10
	if d%2==0:
		s=s+d
	n=n//10
print("Sum:",s)