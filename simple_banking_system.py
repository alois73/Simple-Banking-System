accounts = {}
transactions = {}

def show_menu():
    print("[1] Display accounts")
    print("[2] Add account")
    print("[3] Check balance")
    print("[4] Deposit")
    print("[5] Withdraw")
    print("[6] Display transactions")
    print("[7] Exit")

def create():
    acc_num = input("Enter account number: ")
    accounts.update({acc_num: 0})
    print('New account added')

def check_balance():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print("Account found...")
        print(accounts[acc_num])
    else:
        print("Account not found")

def deposit():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = int(input("Enter amount: "))
        accounts.update[acc_num] += amount
        transactions.update({acc_num: '+' + amount})
    else:
        print("Account not found")

def withdraw():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = int(input("How much to withdraw: "))
        if accounts[acc_num] < amount:
            print("Insuficent balance")
        elif accounts[acc_num] == amount:
            print("Your balance is now 0")
            accounts[acc_num] -= amount
            transactions.update({acc_num: '-' + amount})
        else:
            print("Withdrawl successful")
            accounts[acc_num] -= amount
            transactions.update({acc_num: '-' + amount})

def show_transactions():
    print(transactions)

def show_accounts():
    print(accounts)

def main():
    closed = False
    show_menu()
    while not closed:
        option = int(input("Enter option: "))
        if option == 1:
            show_accounts()
        elif option == 2:
            create()
        elif option == 3:
            check_balance()
        elif option == 4:
            deposit()
        elif option == 5:
            withdraw()
        elif option == 6:
            show_transactions()
        elif option == 7:
            closed = True
            print("Goodbye")
        else:
            print("Invalid option")

main()
