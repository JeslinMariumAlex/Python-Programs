num=int(input("Enter the number:"))
sum=0
product=1
while num!=0:
	r=num%10
	sum=sum+r
	product=product*r
	num=num//10
if sum==product:
	print("Spy number")
else:
	print("Not a Spy number")