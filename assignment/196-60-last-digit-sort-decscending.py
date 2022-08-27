

from functools import cmp_to_key


nums = [1243, 1169, 290, 865, 1208]


def last_digit(n):
    s = str(n)
    last = int(s[len(s) - 1])
    return last


def sort_fn(a, b):
    return last_digit(b) - last_digit(a)


def sort_by_last_digit_descending(nums):
    return sorted(nums, key=cmp_to_key(sort_fn))


print(sort_by_last_digit_descending(nums))
