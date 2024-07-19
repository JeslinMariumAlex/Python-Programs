password=["abc","efg","hjk","xyz"]
class passwordmanager:
    def __init__(self,password):
        self.password=password
        self.l=len(self.password)
    def set_password(self):
        st=input("Enter your password")
        if st not in self.password:
            self.password.append(st)
            print("List updated",self.password)
        else:
            print("Duplication")
            print(self.password)
    def get_password(self):
        current_password=self.password[self.l-1]
        print("Current pasword:",current_password)
    def is_correct(selfself):
        st=input("Enter your password")
        if st==self.password[-1]:
            print('True')
        else:
            print("False")
ob=passwordmanager(password)
ob.get_password()
ob.set_password()
ob.is_correct()










