items=int(input("Enter the number of items:"))
if items<10:
	Totalcost=items*12
elif 10<items<99:
	Totalcost=items*10
elif items>100:
	Totalcost=items*7
print("Totalcost=",Totalcost)
