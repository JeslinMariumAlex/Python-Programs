credit=int(input("Enter the credit:"))
if credit<=23:
	print("Freshman")
elif 24<credit<53:
	print("Sophomore")
elif 54<credit<83:
	print("Junior")
elif credit>84:
	print("Senior")
else:
	print("Invalid entry")
