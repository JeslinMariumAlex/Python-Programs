num=int(input("Enter the number:"))
sum=0
square=num*num
while square!=0:
	r=square%10
	sum=sum+r
	square=square//10
if num==sum:
	print("Neon number")
else:
	print("Not a Neon number")