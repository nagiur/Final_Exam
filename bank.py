class Bank:
    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
        self.admins = []
        self.users = []
        self.total_available_balance = 50000
        self.total_loan = 0
        self.loan_feature = True

    def __repr__(self) -> str:
        return f'{self.bank_name} \n----------'

    
