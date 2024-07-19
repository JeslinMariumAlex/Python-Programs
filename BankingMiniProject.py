import pickle


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name):
        if account_number in self.accounts:
            print("Account with that name already exists.")
        else:
            self.accounts[account_number] = 0
            print(f"Account created for {name}.")

    def deposit(self, account_number, name, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number] += amount
                print(f"Rs.{amount} deposited into {name}'s account.")
            else:
                print("Invalid amount. Please enter a positive value.")
        else:
            print(f"No account found for {name}.")

    def withdraw(self, account_number, name, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount > 0:
                self.accounts[account_number] -= amount
                print(f"Rs.{amount} withdrawn from {name}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print(f"No account found for {name}.")

    def check_balance(self, account_number, name):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Account balance for {name}: Rs.{balance}")
        else:
            print(f"No account found for {name}.")

    def close_account(self, account_number, name):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account closed successfully for {name}.")
        else:
            print(f"Account {name} not found.")

    def save_data(self, bank_file):
        with open(bank_file, 'wb') as file:
            pickle.dump(self.accounts, file)
        print("Data saved successfully.")

    def load_data(self, bank_file):
        try:
            with open(bank_file, 'rb') as file:
                self.accounts = pickle.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found.")


bank = Bank()

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Close Account ")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number:")
        name = input("Enter account holder name: ")
        bank.create_account(account_number, name)
    elif choice == "2":
        account_number = input("Enter account number: ")
        name = input("Enter account holder name: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_number, name, amount)
    elif choice == "3":
        account_number = input("Enter account number: ")
        name = input("Enter account holder name: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(account_number, name, amount)
    elif choice == "4":
        account_number = input("Enter account number: ")
        name = input("Enter account holder name: ")
        bank.check_balance(account_number, name)
    elif choice == "5":
        account_number = input("Enter account number:")
        name = input("Enter account holder name: ")
        bank.close_account(account_number, name)
    elif choice == "6":
        bank_file = input("Enter the filename to save the data: ")
        bank.save_data(bank_file)
    elif choice == "7":
        bank_file = input("Enter the filename to load the data: ")
        bank.load_data(bank_file)
    else:
        print("Invalid choice")
