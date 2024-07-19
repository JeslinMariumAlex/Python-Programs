BS=int(input("Enter the Basic Salary:"))
if BS<10000:
	HRA=(2*BS)/100
	DA=(2.5*BS)/100
	PF=(3*BS)/100
elif 10000<BS<17000:
	HRA=(3*BS)/100
	DA=(3.5*BS)/100
	PF=(4.2*BS)/100
elif 17000<BS<23000:
	HRA=(4.4*BS)/100
	DA=(4.1*BS)/100
	PF=(4.7*BS)/100
else:
	HRA=(5.2*BS)/100
	DA=(4.9*BS)/100
	PF=(5.5*BS)/100
Netsalary=HRA+DA+BS-PF
print("Netsalary=",Netsalary)


      
