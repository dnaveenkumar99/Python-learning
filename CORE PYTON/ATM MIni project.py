import time
password=1234
Balance=20000
print("Welcome to Pentagon ATM")
print("Insert your card")
print("Press 1.yes 2.No")
card=int(input())
if card==1:
    print("select the language")
    print("Press 1.English 2.Kannada 3.Telugu")
    lang=int(input())
    if lang==1:
        print("enter ur pin")
        pin=int(input())
        if pin==password:
            print("select the option")
            print("press 1.Balance enq 2.Withdrawl")
            choice=int(input())
            if choice==1:
                print("Your available balance is",Balance)
            elif choice==2:
                print("enter the amount")
                amt=int(input())
                print("Transaction is Proccessing")
                time.sleep(5)
                print("plz collect your cash")
                time.sleep(4)
                print("do you want to check your balance")
                print("press 1.yes 2.no")
                choice1=int(input())
                if choice1==1:
                    print("your available balance is",Balance-amt)
                    print("Thank you visit again")
                else:
                    print("Thank you visit again")
            else:
                print("select the correct opt")
        else:
            print("Incorrect pin")
    else:
        print("plz select only english")
else:
    print("insert ur card properly")
