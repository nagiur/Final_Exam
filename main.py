from bank import Bank
from admin import Admin
from user import User

def new_line():
    print()

def main():
    print("\t Banking Management System")
    print("---------------------------------------------")

    brac_bank = Bank("BRAC Bank")
    
    admin = Admin(1, "Admin_one")
    admin.create_account(brac_bank)
    admin.total_available_balance(brac_bank)
    admin.total_loan_amount(brac_bank)
    admin.set_loan_feature(brac_bank, True)
    
    new_line()
    user_1 = User(1, "Nagiur Rahaman")
    user_1.create_account(brac_bank)

    user_1.deposit(2500, brac_bank)
    user_1.withdraw(1300, brac_bank)
    user_1.check_balance()

    new_line()
    user_2 = User(2, "Akash Ali")
    user_2.create_account(brac_bank)

    user_1.transfer(400, user_2)
    user_2.check_balance()

    admin.set_loan_feature(brac_bank, False)
    user_1.transfer(300, user_2)

    new_line()
    user_1.check_balance()
    user_2.check_balance()

    new_line()
    user_1.get_transaction_history()
    user_2.get_transaction_history()


    new_line()
    print(f"Admins List of {brac_bank.bank_name}: ", brac_bank.admins)
    print(f"Users List of {brac_bank.bank_name}: ", brac_bank.users)


if __name__ == '__main__':
    main()