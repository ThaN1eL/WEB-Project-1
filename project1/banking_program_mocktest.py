                #"""MockTest from scratch: Banking Program Test"""

def check_balance(balance):
    print(f"Your Balance is ${balance:.2f}")


def deposit(balance):
    try:  
        amounts = float(input("Please Enter the amount: "))
        
        if amounts < 50:
            print("sorry please enter the value greather than 50")
            return 0
        else:
            print(f"your withdrawal ${amounts:.2f} succeed !")
            return amounts
    except ValueError:
        print("Please enter the numeric value")
        return 0
            
def withdraw(balance):
    try:
        amounts = float(input("Please enter the amounts: "))
        
        if amounts > balance:
            print("Innuficient fund")
            return 0
        elif amounts < 50:
            print("Please enter the value greater than  50")
            return 0
        else:
            print(f"Your withdrawal${amounts:.2f} succeed !")
            return amounts
    except ValueError:
        print("Please numeric value")
        return 0
    
def main():
    balance = 0 
    run = True
    
    while run:
        print("1.Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Please choose your desired choice 1 - 4: ")
        
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance += deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            run = False
        else:
            print("Invalid Input !")
            
    print("Thankyou Have a nice day")
            
if __name__ == '__main__': 
    main()