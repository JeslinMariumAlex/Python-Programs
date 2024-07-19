import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="db1")

mycursor = mydb.cursor()
mycursor.execute("select * from student")
res = mycursor.fetchall()
print(res)
for x in res:
    print(x)
