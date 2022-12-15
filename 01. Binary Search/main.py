"""Assignment 1 Binary Search: main.py"""
import numpy as np
import random
import cProfile
import pstats


def create_and_shuffle():
    arr = np.arange(5000)

    lis = [*arr]

    random.shuffle(lis)

    return lis


def binary(arr, x, l, h):
    print(f"BS Function called at low: {l}, high: {h} for number {x}")
    if l > h:
        return False

    else:
        mid = (l + h) // 2
        if x == arr[mid]:
            return mid

        elif x > arr[mid]:
            return binary(arr, x, mid + 1, h)

        else:
            return binary(arr, x, l, mid)


def main():
    # num = int(input("Enter the number to search: "))
    with cProfile.Profile() as pr:
        num = 30

        shuffled_array = create_and_shuffle()

        shuffled_array.sort()

        high = len(shuffled_array)
        low = 0

        i = binary(shuffled_array, num, low, high)

        print(f"Number is at position {i} in array")
        print(f"Number is {shuffled_array[i]}")

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename="BinarySearchMain.prof")


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename="BinarySearch.txt")
