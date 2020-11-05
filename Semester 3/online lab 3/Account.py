class Account:
    def __init__(self, name, balance):
        print("Your current balance is: "+str(balance))
        self.__name = name
        self.__balance = balance

    def cashDepo(self):
        amount = float(input("Enter amount to deposit: "))
        self.__balance += amount

    def cashWith(self):
        amount = float(input("Enter amount to withdraw: "))
        self.__balance -= amount

    def accountInfo(self):
        print("Account title: "+str(self.__name))
        print("Account balance: "+str(self.__balance))

    def display(self):
        while True:
            print("Press 1 for Cash Deposit")
            print("Press 2 for Cash WithDraw")
            print("Press 3 for Cash Current Balance")
            print("Press 4 for Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.cashDepo()

            elif choice == 2:
                self.cashWith()

            elif choice == 3:
                self.accountInfo()

            else:
                break


account = Account("Aneeq", 50000)
account._Account__balance = 10000  # accessing private attributes
account.display()
