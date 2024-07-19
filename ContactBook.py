import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="root")
    cursor = mydb.cursor()
    cursor.execute("Create database contact_book1")
    mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="contact_book1")
    cursor = mydb.cursor()
    cursor.execute("Create table phonebook(name varchar(25),phone_no bigint)")
except:
    print("DB already exists!!!")
    mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="contact_book1")
    cursor = mydb.cursor()


def insert(name, phone_no):
    cursor.execute("select name from phonebook")
    names = cursor.fetchall()
    f = 0
    for i in names:
        if name == i:
            f = 1
    if f == 0:
        cursor.execute("Insert into phonebook(name,phone_no) values(%s,%s)", (name, phone_no))
        mydb.commit()
    else:
        print("Name already exists!!")
        cursor.execute("update phonebook set phone_no=%s where name=%s", (phone_no, name))
        mydb.commit()


def update(data):
    if data == "name":
        old_name = input("Enter old name:")
        cursor.execute("Select name from phonebook where name=%s", old_name)
        sel_name = cursor.fetchall()
        print(sel_name)
        new_name = input("Enter new name:")
        if new_name in sel_name:
            print("Name exists!!")
        else:
            cursor.execute("Update phonebook set name=%s where name=%s", (new_name, old_name))
            mydb.commit()
            print("Updated successfully")
    else:
        print("Can't Update")


def delete(item):
    cursor.execute("Select name from phonebook")
    item_list = cursor.fetchall()
    f = True
    for i in item_list:
        if item in i:
            cursor.execute("delete from phonebook where name=%s,(item)")
            mydb.commit()
            f = False
        if f:
            print("Contact not found")


def display():
    cursor.execute("select * from phonebook")
    contacts = cursor.fetchall()
    print(contacts)


while True:
    print("Menu")
    print("1.Insertion\n2.Updation\n3.Deletion\n4.Display\n5.Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        print("Insert new contact")
        name = input("Enter name:")
        phone_no = input("Enter phone number:")
        insert(name, phone_no)
    elif ch == 2:
        print("Updation")
        data = input("Update name?")
        update(data)
    elif ch == 3:
        print("Deletion")
        item = input("Enter name:")
        delete(item)
        print("Deleted Contact:", item)
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("wrong choice")
