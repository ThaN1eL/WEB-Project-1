                #"""MockTest from scratch: Banking Program Test 3rd ATTEMPT. LAST TRY NO CAP :)"""
# balance, withdraw and deposit

def check_balance(balance):
    print(f"Your Current balance is ${balance:.2f}")
    
def deposit(balance):
    amount = float(input("Please input the amounts"))

    if amount < 50:
       print("please input the value higher than 50")  
       return  0
    else:     
       print(f"Your deposit ${amount:.2f}has been succeed!")
       return amount
   
def withdraw(balance):
    amount = float(input("Please input the amounts"))
    
    if amount > balance:
       print("Inufficient fund")
       return 0
    elif amount > 50:
       print("Please input the amount greater than 50")
       return 0  
    elif amount < 0:
        print("please input the positive amounts :))")
        return 0
    else:
        print(f"Your Withdrawal ${amount:.2f} has been succeed! ")
        return amount
    
    
    
    
def main():
    balance = 0
    run = True
    
    while run:
        print("1. Show Balance:")
        print("2.Deposit:")
        print("3.Withdraw:")
        print("4. Exit")
        
        choice = input("Please select what transaction do you need from 1 - 4 ")
        
        if choice == '1':
            check_balance(balance)      
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
             run = False
        else:
            print("Please select only from  1, 2, 3 or 4")
    print("ThankYou for your today transaction sir") 
                     
if __name__ == '__main__':
    main()