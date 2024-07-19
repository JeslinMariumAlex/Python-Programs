import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="db1")

mycursor = mydb.cursor()
sql = "insert into student(name,address) values (%s,%s)"
val = [("kiran", "Thiruvalla,Pathanamthitta"), ("Aishwarya", "Anchal,klm"), ("Dhanya", "Haripad,Allapuzha")]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
