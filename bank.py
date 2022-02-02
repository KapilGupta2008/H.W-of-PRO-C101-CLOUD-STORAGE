class Bank:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def balance(self):
        print("your account has 1000 r")
    def withdraw(self,amount):
        newamount=1000-amount
        print("your have withdraw amount "+str(amount)+" your remaing balance is "+ str(newamount))

def main():
    
    cardnumber=input("inter your card number")
    pin=input("inter your pin number")

    atm = Bank(cardnumber,pin)
    print("choose your activity")
    print("1.balance 2.cash withdraw")
    user=int(input("enter your choice"))

    if(user==1):
        atm.balance()
    elif(user==2):
        amount=int(input("enter your amount"))
        atm.withdraw(amount)
    else:
        print("enter the valid pin")

if __name__ == "__main__":
     main()