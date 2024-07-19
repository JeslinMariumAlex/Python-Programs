import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="db1")

mycursor = mydb.cursor()
mycursor.execute("Create table student (name varchar(25),address varchar(25))")
print("Table Created")
