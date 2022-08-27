def factorial(n):
    if n == 1:
        return n
    return factorial(n - 1) * n


def getN():
    return int(input("Enter a positive integer: "))


n = getN()
result = factorial(n)

print(f"{n}! is {result}")
