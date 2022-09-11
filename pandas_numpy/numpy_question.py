from random import random
from textwrap import fill
import numpy as np

# 1
arr = [np.full(3, range(0, 3)), np.full(
    3, range(3, 6)), np.full(3, range(6, 9))]

print(arr)


# 2

arr_2 = np.random.randint(100, size=(10, 10))

min_value = arr_2.min()
max_value = arr_2.max()

print(min_value, max_value)

# 3

exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

exercise_1[exercise_1 % 2 == 1] = -1

print(exercise_1)

# 4

exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

resized = np.reshape(exercise_2, (3, 3))

print(resized)

# 5: Add 202 to all the values in given array

exercise_3 = np.arange(4).reshape(2, -1)


def add202(x):
    return x + 202


print(list(map(add202, exercise_3)))


# 6

exercise_6 = np.arange(100).reshape(5, -1)

print(exercise_6[0:len(exercise_6[0]), 0:4])
