# To implement bank account, we need class, constructors and methods
# method : deposit(),withdraw(),transfer(),show_balance(),show_transaction(),
class BankAccount:
    def __init__(self,account_holder_name,email,address,contact_no,type_of_acct,age,account_id):
        self.account_holder_name = account_holder_name
        self.email =email
        self.address= address
        self.contact_no = contact_no
        self.type_of_acct =type_of_acct
        self.age = age
        self.account_id = account_id
        self.balance =0

    #methods
    def deposit(self):
            deposit_amt = int(input("Enter the amount you want to deposit: "))
            self.balance +=deposit_amt
            print("The new available balance:",self.balance)

    def withdraw(self):
            withdraw_amt = int(input("Please enter the amount that you want to withdraw: "))
            self.balance-=withdraw_amt
            print("The available balance after withdrawal is : ",self.balance)

    #def show_transaction(self):

    def display(self):
        print(f"Account_ID: {self.account_id}")
        print(f"Name: {self.account_holder_name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Contact No: {self.contact_no}")
        print(f"Account Type: {self.type_of_acct}")
        print(f"Age: {self.age}")
        print(f"Balance: {self.balance}")

