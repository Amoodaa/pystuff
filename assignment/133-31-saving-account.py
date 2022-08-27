current_balance = 1000

print("""
Options:
1. Make a Deposit
2. Make a Withdrawal
3. Obtain Balance
4. Quit
""")


def deposit():
    global current_balance
    deposit_amount = int(input("Enter amount of deposit: "))
    current_balance = current_balance + deposit_amount
    print("Deposit Processed.")


def withdraw():
    global current_balance
    withdrawal_amount = int(input("Enter amount of withdrawal: "))
    if current_balance < withdrawal_amount:
        print(f"Denied. Maximum withdrawal is ${current_balance}.")
        return
    current_balance = current_balance - withdrawal_amount
    print("Withdraw successful.")


def show_balance():
    global current_balance
    print(f"Balance: ${current_balance}")


while True:
    selected_option = int(input("Make a selection from the options menu: "))
    match selected_option:
        case 1:
            deposit()
            break
        case 2:
            withdraw()
            break
        case 3:
            show_balance()
            break
        case 4:
            exit(0)


# PS D:\code\pystuff\assignment> python .\118-34-saving-account.py
# Enter current balance: 1341
# Enter amount of withdrawal: 321
# The new balance is $1020
