# To implement bank account, we need class, constructors and methods
# method : deposit(),withdraw(),transfer(),show_balance(),show_transaction(),

class BankAccount:
    #constructor:intialize the attributes
    #methods will give behaviours for the objects , they can access , modify , and perform actions on attributes.
    def __init__(self,account_id,name,balance):
        self.account_id=account_id #attributes
        self.name=name
        self.balance = balance

    #methods
    def deposit(self):
        acct_id= int(input("Enter the user account id: "))
        if acct_id == self.account_id:
            print("Customer name:",self.name ,"Account_id:",self.account_id,"Account number:",self.account_number,"Available balance:",self.balance)
            #Get the user input how much user want to deposit
            deposit_amt = int(input("Enter the amount you want to deposit: "))
            self.balance +=deposit_amt
            print("The new available balance:",self.balance)
        else:
            print("Provide valid account id!!")

    def withdraw(self):
        acct_id =int(input("Enter the user account id for validation:"))
        if acct_id == self.account_id:
            withdraw_amt = int(input("Please enter the amount that you want to withdraw: "))
            self.balance-=withdraw_amt
            print("The available balance after withdrawal is : ",self.balance)
        else:
            print("Please enter the valid account id! ")

    #def show_transaction(self):


    def show_balance(self):
        #get account_id and validate and print the balance
        acct_id=int(input("Please enter your account id to see your account balance: "))
        if acct_id == self.account_id:
            print("The account number is :",self.account_number ,"and the available balance is :",self.balance)
        else:
            print("Sorry the provided account id is invalid.Please Try again!")
