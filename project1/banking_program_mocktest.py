def show_balance(balance):
    print(f"Your balance is ${balance}")
    
def deposit(balance):
    amount = int(input("Please enter an amounts to be Deposited: "))
    
    if amount < 10:
        print("Please enter amount greater than $10! ")
        return 0
    else:
        print(f"You Succeed Deposit ${amount}")
        return amount
        
def withdraw(balance):
    amounts = int(input("Please enter an amount to be Withdrawal: "))
    
    if amounts > balance:
        print("Insufficient amounts !")
        return 0
    elif amounts < 10:
        print("Please enter amount greater than $10 !")
        return 0
    else:
        print(f"Your Withdrawal Succeed ${amounts}")
        return amounts
        

def main():
    balance = 0
    running = True
    
    while running:
        print("1. Show Balance ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Exit ")
    
        select=input("Select Your Choice from 1 until 4: ")
        
        if select == "1":
            show_balance(balance)
        elif select == "2":
            balance += deposit(balance)
        elif select == "3":
            balance -= withdraw(balance)
        elif select == "4":
            running = False
        else:
            print("Invalid Input. Please select between 1-4")
        
print("Thank You !!! Have a nice day!")
       

if __name__ == '__main__':
    main()
 
        