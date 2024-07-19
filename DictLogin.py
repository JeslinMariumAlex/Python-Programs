n = int(input("Enter the number of Users:"))
login = dict()
for i in range(n):
    user_name = input("Enter the user name:")
    pass_word = input("Enter the password:")
    login[user_name] = pass_word
print("Dictionary", login)
print("Login")
while True:
    username = input("Enter username or Q to quit:")
    if username == 'Q' or username == 'q':
        print("Exiting")
        break
    elif username in login:
        password = input("Enter the password: ")
        if login[username] == password:
            print("You are now logged into the system")
        else:
            print("Invalid password")
    else:
        print("You are not valid user")
