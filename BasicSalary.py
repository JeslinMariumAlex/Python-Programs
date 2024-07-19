BS=int(input("Enter the Basic Salary:"))
Hra=0.03*BS
DA=0.035*BS
PF=0.04*BS
Allowance=2500
print("Hra:",Hra)
print("DA:",DA)
print("PF:",PF)
print("Allowance:",Allowance)
NetSalary=BS+DA+Hra+Allowance-PF
print("Net Salary:",NetSalary)

