#Bank Account Manager --> is a project used to handle
#Create bank account class
#Create transaction class
#Handle all the data using database scheme.

from bankAccount import BankAccount
from bank import Bank

def main():
    while True:
        print("\nOptions: create | deposit | withdraw | display | exit")
        choice = input("Choose an option: ").lower()
        if choice == 'create':
            Bank.create_account()
        elif choice == 'deposit':
            #ask for account id
            acc_id= int(input("Please enter the account id:"))
            #Get the account object
            account = Bank.accounts.get(acc_id)
            if account:
                account.deposit()
            else:
                print("Account not found!")
        elif choice == 'withdraw':
            acc_id = int(input("Please enter the account id:"))
            # Get the account object
            account = Bank.accounts.get(acc_id)
            if account:
                account.withdraw()
            else:
                print("Account not found!")
        elif choice == 'display':
            for acc in Bank.accounts.values():
                 acc.display()
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Try again.")

# This is the main entry point
if __name__ == "__main__":
    main()


