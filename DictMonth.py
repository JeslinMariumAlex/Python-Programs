month = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
         "September": 30, "October": 31, "November": 30, "December": 31}
mon = input("Enter the name of the month:")
if mon in month:
    print("No of days in ", mon, "is", month[mon])
else:
    print("Not Present")
print("Sorted keys")
lst = month.keys()
lst = list(lst)
lst.sort()
print("Sorted list is", lst)
print("Month containing 31 days")
for keys, values in month.items():
    if values == 31:
        print(keys)
