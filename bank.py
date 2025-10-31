#write login for bank class

class Bank:
    def __init__(self,account_holder_name=" ",email=" ",address=" ",contact_no=" ",type_of_acct=" ",age=" "):
        self.account_holder_name = account_holder_name
        self.email =email
        self.address= address
        self.contact_no = contact_no
        self.type_of_acct =type_of_acct
        self.age = age


    #Methods
    def create_account(self):
        self.age = int(input("Please enter your age: "))
        if self.age >18:
            self.account_holder_name = input("Please enter your name: ")
            self.address =input("Please enter your address: ")
            self.email = input("Please enter your email address: ")
            self.contact_no = int(input("Please enter your contact number: "))
            self.type_of_acct = input("Please provide whether do you need savings or checking account: ")
            print("\nAccount Created Successfully!!")
            print("Account_holder name:",self.account_holder_name)
            print("Address: ",self.address)
            print("Email: ",self.email)
            print("Contact_No: ",self.contact_no)
            print("Account_type: ",self.type_of_acct)
            print("Customer age: ",self.age)
        else:
            print("You must be 18 or Older to create an account.")







