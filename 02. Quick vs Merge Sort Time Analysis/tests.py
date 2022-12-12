"""Assignment 2 Quick Vs Merge Sort Time Analysis: tests.py"""
import numpy as np
import random


def create_test_case(x: int):
    i = random.randint(0, 1000)

    arr = np.arange(x, x + i)

    arr = [*arr]

    random.shuffle(arr)

    return arr


def create_best_case(x: int):
    i = random.randint(0, 1000)

    arr = np.arange(x, x + i)

    arr = [*arr]

    return arr


def create_worst_case(x: int):
    i = random.randint(0, 1000)

    arr = np.arange(x, x + i)

    arr = [*arr]

    arr.reverse()

    return arr


if __name__ == "__main__":
    case1 = create_test_case(30)
    case2 = create_test_case(50)
    case3 = create_test_case(90)
    case4 = create_test_case(20)
    case5 = create_test_case(40)

    print(case1)
    print(case2)
    print(case3)
    print(case4)
    print(case5)
