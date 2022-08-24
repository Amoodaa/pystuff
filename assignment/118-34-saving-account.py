current_balance = int(input('Enter current balance: '))
withdrawal = int(input('Enter amount of withdrawal: '))

balance = current_balance - withdrawal

if withdrawal > current_balance:
    print("Withdrawal denied.")
else:
    print(f"The new balance is ${balance}")

# PS D:\code\pystuff\assignment> python .\118-34-saving-account.py
# Enter current balance: 1341
# Enter amount of withdrawal: 321
# The new balance is $1020
