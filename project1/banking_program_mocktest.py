                #"""MockTest from scratch: Banking Program Test 5th ATTEMPT. :)"""
# balance, deposit and withdraw
#using define function

def balance_inqury(balance):
    print(f"your remaining balance is ${balance}")
    
def deposit(balance):
   try:
        amount = int(input("please enter the valid amount to be deposited: "))
    
        if amount < 0:
            print("please input the value greater than 0 !")
            return 0
        else:
            print(f"Your deposit ${amount} has been succeed ")
            return amount
   except ValueError:
      print("please enter numeric value")
      return 0
    
def withdraw(balance):
    try:
        amount = int(input("please enter the valid amount to withdraw: "))
        
        if amount > balance:
            print("innuficient fund")
            return 0
        elif amount < 0:
            print("please input the value greater than 0")
            return 0
        else:
            print(f"your withdrawal ${amount} has been succed ")
            return amount
    except ValueError:
        print("Please ente numeric value")
        return 0
        
def main():
    balance = 0
    run = True
    
    while True:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("please select from 1, 2 ,3 or 4: ")

        if choice == '1':
            balance_inqury(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            run = False
        else:
            print("please enter the numeric value from 1,2,3 or 4")
    print(" Thank you for your Transaction sir, Have a good day :)")
    
if __name__ == '__main__':
    main()    
            