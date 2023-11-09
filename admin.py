from user import User

class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def create_account(self, bank):
        bank.admins.append(self.name)
        print(f"Admin:  account has been created to {bank.bank_name}")

    def total_available_balance(self, bank):
        print(f"Total available-balance in {bank.bank_name}: ${bank.total_available_balance}")

    def total_loan_amount(self, bank):
        print(f"Total loan amount in {bank.bank_name}: ${bank.total_loan}")

    def set_loan_feature(self, bank, status):
        bank.loan_feature = status
        print(f"Loan feature : {'Enabled' if status else 'Disabled'} for {bank.bank_name}")
