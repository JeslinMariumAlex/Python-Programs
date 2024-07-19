CU=int(input("Enter the Consumed Unit:"))
if CU<100:
	ElectricityBill=CU*0.5
elif CU<200:
	ElectricityBill=(100*0.5)+(CU-100)*1.5
elif CU<500:
	ElectricityBill=(100*0.5)+(100*2)+(CU-200)*3
else:
	ElectricityBill=(100*0.5)+(200*3.5)+(200*4.6)+(CU-500)*6.6
print("Electricity Bill=",ElectricityBill)