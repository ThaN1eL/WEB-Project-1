# PROJECT#1 Python Banking Program 
#12/27/2024 ADD FUND_TRANFER
#12/28/2024 ADD ERROR HANDLING/show withdrawal/deposit success message

def show_balance(balance):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Your Balance is ${balance:.2f}")
    print("$$$$$$$$$$$$$$$$$$$$$$$")

def show_success_message(message):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print(message)
    print("$$$$$$$$$$$$$$$$$$$$$$$")

def deposit(balance):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    try:
        amount = float(input("Please enter an amount to be Deposited: "))
        print("$$$$$$$$$$$$$$$$$$$$$$$")
    
        if amount < 0:
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            print("Sorry, please enter the valid amount :)")
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            return 0
        else:
            show_success_message(f"Deposit of ${amount:.2f} succeeded !")
            return amount
    except ValueError:
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("Invalid Input. Please enter numeric Value.")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    

def withdraw(balance):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    try:
        amounts = float(input("Please enter an amount to be withdrawn: "))
        print("$$$$$$$$$$$$$$$$$$$$$$$")

        if amounts > balance:
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            print("Insufficient funds")
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            return 0
        elif amounts < 0:
            print("Sorry, amount must be greater than 0 :) ")
            return 0
        else:
            show_success_message(f"Withdrawal of ${amounts:.2f} succeeded !")
            return amounts
    except ValueError:
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("Invalid input. Please enter a numeric value.")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    
def fund_tranfer(balance):
    try:
        amounts = float(input("Please enter an amount to Tranfer: "))  
        if amounts > balance:
            print('Insufficient funds')
            return 0
        elif amounts < 0:
            print("Sorry, amount must be greater than 0 :) ")
            return 0 
        else:
            while True: 
                bank_number = input("Please Enter the valid Account number to tranfer: ")
                if bank_number.isdigit() and len(bank_number) == 10:
                    print(f"Tranfer of {amounts} to bank number {bank_number} is succed !")
                    return amounts
                else:
                    print("Invalid bank number. Please enter a valid 10-digit numeric bank number.")
    except ValueError:
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("Invalid input. Please enter a numeric value for the amount.")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    
def main():    
    balance = 0
    is_running = True

    while is_running:
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("    Banking Program    ")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("1.Show Balance")
        print("2.Deposit")
        print("3. Withdraw")
        print("4. Fund Tranfer")
        print("5.Exit")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': #show balance
            show_balance(balance)
        elif choice == '2': #input deposit
            balance += deposit(balance)
        elif choice == '3': #input withdraw
            balance -= withdraw(balance)
        elif choice == '4': #input fund_tranfer
            transferred_amount = fund_tranfer(balance)
            if transferred_amount > 0:
                balance -= transferred_amount
        elif choice == '5':
            is_running = False
        else:
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            print("Invalid choice. Please enter a number between 1 and 5")
            print("$$$$$$$$$$$$$$$$$$$$$$$")
    
    print("$$$$$$$$$$$$$$$$$$$$$$$")        
    print("Thank You! Have a nice day!")
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    
if __name__ == '__main__':
    main()