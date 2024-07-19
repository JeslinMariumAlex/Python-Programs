n=int(input("Enter the nummber:"))
s=0
while n!=0:
	d=n%10
	s=s+d
	n=n//10
print("Sum:",s)
