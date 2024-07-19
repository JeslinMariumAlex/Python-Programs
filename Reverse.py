n=int(input("Enter the Number:"))
s=0
print("Reversed number:")
while n!=0:
	d=n%10
	s=(s*10)+d
	n=n//10
print(s)


 