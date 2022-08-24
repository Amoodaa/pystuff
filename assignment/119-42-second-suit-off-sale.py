first_shirt_cost = float(input('Enter first shirt cost: '))
second_shirt_cost = float(input('Enter second shirt cost: '))

discount = (first_shirt_cost
            if first_shirt_cost < second_shirt_cost
            else second_shirt_cost) * 0.5

total_cost = first_shirt_cost + second_shirt_cost - discount

print(f"Cost of the two suits is ${total_cost}")

# Enter first shirt cost: 378.50
# Enter second shirt cost: 495.99
# Cost of the two suits is $685.24
