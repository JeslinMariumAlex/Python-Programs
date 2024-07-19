import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="db1")

mycursor = mydb.cursor()
mycursor.execute("select * from student where name in ('kiran','Dhanya')")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
