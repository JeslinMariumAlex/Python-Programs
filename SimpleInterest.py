p=int(input("Principle Amount:"))
r=int(input("Rate Of Interest:"))
n=int(input("Number of years:"))
SI=(p*r*n)/100
CI=p*(1+(r/100))**n
print("Simple Interest:",SI)
print("Compound Interest:",CI)