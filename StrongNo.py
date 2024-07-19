num=int(input("Enter the number:"))
temp=num
sum=0
while num!=0:
	d=num%10
	fact=1
	i=1
	while i<=d:
		fact=fact*i
		i=i+1
	sum=sum+fact
	num=num//10
if sum==temp:
	print("Strong number")
else:
	print("Not Strong number")