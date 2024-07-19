import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="db1")

mycursor = mydb.cursor()
sql = "insert into student(name,address) values (%s,%s)"
val = ("kiran", "tvm")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
