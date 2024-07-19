num=int(input("Enter the number:"))
count=2
flag=1
while count<num:
	if num%count==0:
		flag=0
	count=count+1
if flag==1:
	print("Prime number")
else:
	print("Not Prime number")
	
