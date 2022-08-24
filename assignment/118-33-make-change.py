amount = input('Enter weight in pounds: ')
tendered_change = input('Enter payment in dollars: ')

change = int(tendered_change) - int(amount) * 2.5

if change < 0:
    print(f"You owe ${change} more")
else:
    print(f"Your change is ${change}")

# PS D:\code\pystuff> python .\118-33-make-change.py\
# Enter weight in pounds: 2
# Enter payment in dollars: 6
# Your change is $1.0
