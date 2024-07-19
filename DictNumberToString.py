number_names = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                9: "Nine"}
number = input("Enter the number:")
result = " "
for i in number:
    key = int(i)
    value = number_names[key]
    result += " " + value
print("The number is:", number)
print("The Number Name is:", result)
