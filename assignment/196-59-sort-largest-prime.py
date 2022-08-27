from functools import cmp_to_key
from math import sqrt


def is_prime(n):
    for a in range(2, int(sqrt(n))):
        if n % a == 0:
            return False
    return True


def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


nums = [1243, 1169, 290, 865, 1208]


def sort_fn(a, b):
    a_largest_factor = largest_prime_factor(a)
    b_largest_factor = largest_prime_factor(b)
    return a_largest_factor - b_largest_factor


def sort_by_largest_prime_factor(nums):
    return sorted(nums, key=cmp_to_key(sort_fn))


print(sort_by_largest_prime_factor(nums))
