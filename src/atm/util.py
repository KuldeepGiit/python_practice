class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        print(id(self))

        self.menu()
    def menu(self):

        user_input = print('''
                    how would you like to proceed?
                    1. press 1 to create pin
                    2. press 2 to deposit
                    3. press 3 to withdraw
                    4. press 4 to check balance
                    5. press 5 to exit 
        ''')
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("get lost")
    def create_pin(self):
        self.pin = input("Enter your pin")
        print("pin set successfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            withdraw = int(input("Enter amount to withdraw"))
            if self.balance >= withdraw:
                self.balance = self.balance - withdraw
                print("Withdraw successful")
            else:
                print("entered amount cant be withdrawed")
        else:
            print("Invalid pin")
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")

sbi = Atm()
sbi.create_pin()
sbi.deposit()


