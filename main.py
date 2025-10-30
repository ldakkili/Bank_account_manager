#Bank Account Manager --> is a project used to handle
#Create bank account class
#Create transaction class
#Handle all the data using database scheme.
from bankAccount import BankAccount

if __name__ =="__main__":
    # creating objects
    bank_acc1 = BankAccount(456,"LikithaDakkili",500034564,10000)
    bank_acc2 =BankAccount(345,"KanchanaMopuru",500037787,15000)

    #calling methods
    bank_acc1.show_balance()
    bank_acc2.show_balance()

