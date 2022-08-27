n = int(input("How many numbers do you want to enter? "))

set = [0] * n

for x in range(n):
    set[x] = int(input("Enter a number: "))

is_odd = len(set) % 2 == 1

if_even = set[len(set)//2]
if_odd = (set[len(set)//2] + set[len(set)//2 + 1]
          ) / 2

median = if_odd if is_odd else if_even

print(f"Median is: {median:.2f}")
