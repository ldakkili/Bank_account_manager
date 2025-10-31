#write login for bank class
from bankAccount import BankAccount
import random

class Bank:
    accounts = { }

    @staticmethod
    def random_account_id( ):
        account_id = random.randint(1000, 5000)
        while account_id in Bank.accounts:
             account_id = random.randint(1000, 5000)
        return account_id


# Dictionary to store all accounts

    @staticmethod
    def create_account():
        age = int(input("Please enter your age: "))
        if age <18:
            print("You must be 18 or Older to create an account.")
            return  None

        account_holder_name = input("Please enter your name: ")
        address =input("Please enter your address: ")
        email = input("Please enter your email address: ")
        contact_no = int(input("Please enter your contact number: "))
        type_of_acct = input("Please provide whether do you need savings or checking account: ")

        account_id = Bank.random_account_id()
        new_account = BankAccount(account_holder_name,email,address,contact_no,type_of_acct,age,account_id)
        Bank.accounts[account_id] =new_account

        print(f"\nAccount Created Successfully!!\n Account ID: {account_id}")
        return account_id


