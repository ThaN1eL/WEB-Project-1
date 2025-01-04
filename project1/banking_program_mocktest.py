                #"""MockTest from scratch: Banking Program Test 4th ATTEMPT. :)"""
# balance, withdraw and deposit
#using define function

def balance_check(balance):
    print(f"YourBalance is ${balance}")
    
def deposit(balance):
    amount = int(input("please input the value you want to deposited: "))
    
    if amount < 0:
        print("please input the value greater than 0")
        return 0
    else:
        print(f"your deposit ${amount} has been succeed!")
        return amount
    
def withdraw(balance):
    amount = int(input("please input the value you want to withdraw'ed: "))
    
    if amount > balance:
        print("innuficient fund")
        return 0
    elif amount < 0:
        print("please input the value greater than 0")
        return 0
    else:
        print(f"your withdrawal ${amount} has been succeed !")
        return amount
    
    
def main():
    balance = 0
    run = True
    
    while run:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
        choice = input("please select your choice from 1, 2 , 3 or 4: ")
            
        if choice == '1':
            balance_check(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            run = False
        else:
            print("Please select 1,2,3 or 4")
        
    print("Thank you for using this services my bro")
        
if __name__ == '__main__':
    main()