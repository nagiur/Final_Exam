class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.balance = 0
        self.loan = 0
        self.transaction_history = []

    def create_account(self, bank):
        bank.users.append(self.name)
        print(f"User: account has been created to {bank.bank_name}")


    def deposit(self, amount, bank):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        bank.total_available_balance += amount
    
    def withdraw(self, amount, bank):
        if self.balance >= amount:
            if bank.total_available_balance < amount:
                print(f"The {bank.bank_name} is Bankrupt!")
                return

            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            bank.total_available_balance -= amount
        else:
            print(f"Insufficient money on : {bank.bank_name} ")

    def transfer(self, amount, user):
        if self.balance >= amount:
            user.balance += amount
            self.balance -= amount
            self.transaction_history.append(f"Transfer: ${amount}, to {user.name}")
            user.transaction_history.append(f"Transfer: ${amount}, From {user.name}")
        
        else:
            print(f"Insufficient Money on : {self.name}, Can not transfer!" )

    def take_loan(self, amount, bank):
        if bank.loan_feature:
            max_loan_available = self.balance * 2
            if amount < max_loan_available:
                bank.total_available_balance -= amount
                bank.total_loan += amount
                self.loan += amount
                # self.balance += amount
                self.transaction_history.append(f"Take loan: {self.loan}")
            else:
                print(f"Your Available-loan: {max_loan_available}, But you requested more then it!")
        else:
            print(f"Loan feature is OFF for {bank.bank_name}")


    def check_balance(self):
        print(f"{self.name}'s balance: ${self.balance}, loan: ${self.loan}")
        
    
    def get_transaction_history(self):
        print(f"Transaction History for {self.name}: ")
        for history in self.transaction_history:
            print("\t", history)

    

