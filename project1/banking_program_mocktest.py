                #"""MockTest from scratch: Banking Program Test 6th ATTEMPT. :)"""
# balance, deposit , withdraw ,fund_tranfer, bank_number and ErrorHandling
#using define function

def balance_check(balance):
    print(f"Your current balance is ${balance}")
    
def deposit(balance):
    try:
        amount = int(input("please input the amount you want to deposit: "))
        
        if amount <= 0:
            print("Please input amount greater than 0")
            return 0
        else:
            print(f"Congratulation you have succeed saving your money ${amount}")
            return amount
    except ValueError:
        print("Please enter the numeric value")
        return 0
    
def withdraw(balance):
    try:
        amount = int(input("please input the amountyou want to withdraw: "))
        
        if amount > balance:
            print("innuficient balance")
            return 0
        elif amount <= 0:
            print("please input the amount greater than 0")
            return 0
        else:
            print(f"Congratulation you have been succed withdrawal your money ${amount}")
            return amount
    except ValueError:
        print("Please enter numeric value")
        return 0
def fund_tranfer(balance):
    try:
        amount = int(input("please input the amount you want to tranfer: "))
        
        if amount > balance:
            print("innuficient fund")
            return 0
        elif amount <= 0:
            print("please enter the amounter greater than 0")
            return 0
        else:
            while True:
                bank_number = input("please input the 5-digit bank number ")
                if bank_number.isdigit() and len(bank_number) == 5:
                    print(f"Congratulation you have been succeed execute fund transfer ${amount} to the {bank_number}")
                    return amount
                else:
                    print("please enter 5 Digit bank number bro, you cant read ?!? huh???")
                    return 0
    except ValueError:
        print("please input the numeric value")
        return 0

def main():
    balance = 0
    run = True
    
    while run:  
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Fund Tranfer")
        print("5. Exit")
        
        choice = input("please input, what transaction do you want to execute: ")
        
        if choice == '1':
            balance_check(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            balance -= fund_tranfer(balance)
        elif choice == '5':
            run = False
        else:
                print("Please enter the right choice from 1,2,3,4 or 5 :)")
    print("ThankYOU for the today transaction :)")


if __name__ == '__main__':
    main()