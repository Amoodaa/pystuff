current_balance = 1000

print("""
Options:
1. Make a Deposit
2. Make a Withdrawal
3. Obtain Balance
4. Quit
""")


def makeDeposit():
    global current_balance
    amountToDeposit = int(input("Enter amount of deposit: "))
    current_balance = current_balance + amountToDeposit
    print("Deposit Processed.")


while True:
    selectedOption = int(input("Make a selection from the options menu: "))
    match selectedOption:
        case 1:
            makeDeposit()
            break
        case 2:
            break
        case 3:
            break


# PS D:\code\pystuff\assignment> python .\118-34-saving-account.py
# Enter current balance: 1341
# Enter amount of withdrawal: 321
# The new balance is $1020
