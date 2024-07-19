import pickle

fp = open("student", "wb")
for i in range(0, 3):
    name = input("Name:")
    rollno = int(input("Rollno:"))
    phone = int(input("Phone:"))
    data = [rollno, name, phone]
    pickle.dump(data, fp)
print("Successfully completed")
fp.close()
fp = open("student", "rb")
i = 1
while i <= 3:
    lst = pickle.load(fp)
    print(lst[0])
    print(lst[1])
    print(lst[2])
    i = i + 1
