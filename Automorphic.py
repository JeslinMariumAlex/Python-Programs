n=int(input("Enter the number:"))
num=n
t=10
square=num*num
flag=False
while n>0:
	r=square%t
	if num==r:
		flag=True
		break
	n=n//10
	t=t*10
if flag==True:
	print("Automorphic number")
else:
	print("Not Automorphic number")
	


