"""Assignment 2 Quick Vs Merge Sort Time Analysis: merge.py"""
def mergesort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr

    else:
        mid = len(arr) // 2
        return merge(mergesort(arr[:mid]), mergesort(arr[mid + 1 :]))


def merge(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    return arr

