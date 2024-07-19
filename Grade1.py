#Grade of a student using nested if

p=int(input("Enter the mark of Physics:"))
c=int(input("Enter the mark of Chemistry:"))
m=int(input("Enter the mark of Maths:"))
per=((p+c+m)/300)*100
print("Percentage",per)
if(p>45 and c>45 and m>45):
	if(per>=90):
		print("Grade:A")
	elif(per>=80):
		print("Grade:B")
	elif(per>=70):
		print("Grade:C")
	elif(per>=60):
		print("Grade:D")
	elif(per>=50):
		print("Grade:E")
	else:
		print("Grade:F")
else:
	print("Grade:F")
