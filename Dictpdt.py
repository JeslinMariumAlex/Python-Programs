n = int(input("Enter the number of Products:"))
price = dict()
for i in range(0, n):
    product_name = input("Enter the name of product:")
    price[product_name] = int(input("Enter its price:"))
print("Shop is ready")
print("Check for the availability of product")
while True:
    check_product = input("Enter the product or q to exit:")
    if check_product == "q" or check_product == "Q":
        break
    if check_product in price:
        print("Price of", check_product, "is", price[check_product])
    else:
        print(check_product, "not available")
print("Checking the price list")
amount = int(input("Enter the amount:"))
print("Products below the price", amount, "is")
for i in price:
    if price[i] < amount:
        print(i, ":", price[i])
