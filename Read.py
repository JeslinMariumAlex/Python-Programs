fp = open('sales', 'w')
str = 'hai'
str1 = "hello"
str2 = "welcome"
fp.write(str)
fp.write("\n")
fp.write(str1)
fp.write("\n")
fp.write(str2)
fp.close()
fp = open("sales", "r")
# str=fp.read()
# print("Reading")
# print(str)
# __________________
# str=fp.readline()
# print("Reading")
# print(str)
# str=fp.readline()
# print("Second line")
# print(str)
# __________________-
str = fp.readlines()
print("Reading")
print(str)
print(type(str))
