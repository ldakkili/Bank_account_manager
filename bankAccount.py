# To implement bank account, we need class, constructors and methods
# method : deposit(),withdraw(),zelle(),show_balance(),show_transaction(),

class BankAccount:
    #constructor:intialize the attributes
    #methods will give behaviours for the objects , they can access , modify , and perform actions on attributes.
    def __init__(self,account_id,name,account_number,balance):
        self.account_id=account_id #attributes
        self.name=name
        self.account_number=account_number
        self.balance = balance

    #methods

    def show_balance(self):
        print("The account number is :",self.account_number ,"and the available balance is :",self.balance)
