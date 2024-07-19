n=int(input("Enter the number:"))
rev=0
temp=n
while n!=0:
	d=n%10
	rev=(rev*10)+d
	n=n//10
if rev==temp:
	print("Palindrome")
else:
	print("Not a palindrome")