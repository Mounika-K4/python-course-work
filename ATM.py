data = {
    12345: {'pin': 673, 'balance': 8435, 'history': []},
    23456: {'pin': 143, 'balance': 3428, 'history': []},
    67891: {'pin': 103, 'balance': 1256, 'history': []},
    98765: {'pin': 108, 'balance': 3478, 'history': []},
    45674: {'pin': 105, 'balance': 6698, 'history': []},
    36783: {'pin': 104, 'balance': 8358, 'history': []},
}

acc_num = None
login_status = None

def Welcome():
    print('Welcome to the ATM'.center(50, '*'))

def Menu():
    print('\n[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit\n')

def Login():
    account_number = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    global acc_num, login_status
    if account_number in data:
        if data[account_number]['pin'] == pin:
            print("✅ Login Successful")
            acc_num = account_number
            login_status = True
            return True
        else:
            print("❌ Invalid pin")
            login_status = False
            return False
    else:
        print("❌ Invalid account number")
        login_status = False
        return False

def Check_balance():
    if login_status and acc_num:
        print(f'\n💰 Current Balance: {data[acc_num]["balance"]}')
    else:
        print("⚠ You need to login again")

def Deposit():
    if login_status and acc_num:
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            data[acc_num]['balance'] += amount
            data[acc_num]['history'].append(f'Deposited - ${amount}')
            print(f'✅ ${amount} successfully deposited')
        else:
            print("❌ Invalid amount")
    else:
        print("⚠ You need to login again")

def Withdraw():
    if login_status and acc_num:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > 0:
            if data[acc_num]['balance'] >= amount:
                data[acc_num]['balance'] -= amount
                data[acc_num]['history'].append(f'Withdrawn - ${amount}')
                print(f'✅ ${amount} successfully withdrawn')
            else:
                print("❌ Insufficient Balance")
        else:
            print("❌ Invalid amount")
    else:
        print("⚠ You need to login again")

def View_transaction():
    if login_status and acc_num:
        if data[acc_num]['history']:
            print("📜 Transactions History".center(50, '-'))
            for i in data[acc_num]['history']:
                print(i)
            print("End of the history".center(50, '-'))
        else:
            print("No Transactions Yet")
    else:
        print("⚠ You need to login again")

def main():
    Welcome()
    # Force login before menu
    while not Login():
        print("🔁 Try logging in again...\n")

    while True:
        Menu()
        choice = input("Enter choice: ").strip().upper()

        if choice == "C":
            Check_balance()
        elif choice == "D":
            Deposit()
        elif choice == "W":
            Withdraw()
        elif choice == "V":
            View_transaction()
        elif choice == "E":
            print("👋 Thank you for using ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
