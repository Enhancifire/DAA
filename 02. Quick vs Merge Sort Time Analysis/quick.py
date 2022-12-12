"""Assignment 2 Quick Vs Merge Sort Time Analysis: quick.py"""


def quicksort(l, r, arr):
    if len(arr) == 1:
        return arr

    if l < r:
        p = partition(l, r, arr)
        quicksort(l, p - 1, arr)
        quicksort(p + 1, r, arr)
    return arr


def partition(l, r, arr) -> int:
    pivot, pointer = arr[r], l

    for i in range(l, r):
        if arr[i] <= pivot:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

    arr[pointer], arr[r] = arr[r], arr[pointer]
    return pointer
