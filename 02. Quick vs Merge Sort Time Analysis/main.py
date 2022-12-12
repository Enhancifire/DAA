"""Assignment 2 Quick Vs Merge Sort Time Analysis: main.py"""
from quick import quicksort
from merge import mergesort
import random
from tests import create_best_case, create_test_case, create_worst_case
from rich import print
from rich.table import Table
from timeit import default_timer as timer
from datetime import timedelta


def main():

    tb = Table()
    tb.add_column("Test No")
    tb.add_column("Quick Sort")
    tb.add_column("Merge Sort")

    for i in range(0, 5):
        a, b = test(i)
        tb.add_row(str(i), str(a), str(b))

    qb, mb, qw, mw = test_best_and_worst_case()

    tb.add_row("Best Case", str(qb), str(mb))
    tb.add_row("Worst Case", str(qw), str(mw))
    print(tb)


def test(iteration: int):

    rand = random.randint(0, 100)

    test = create_test_case(rand)

    quick_start = timer()
    quicksort(0, len(test) - 1, test)
    quick_end = timer()

    merge_start = timer()
    mergesort(test)
    merge_end = timer()

    return (
        timedelta(seconds=quick_end - quick_start),
        timedelta(seconds=merge_end - merge_start),
    )


def test_best_and_worst_case():
    best_case = create_best_case(10)
    worst_case = create_worst_case(10)

    quick_start = timer()
    quicksort(0, len(best_case) - 1, best_case)
    quick_end = timer()

    merge_start = timer()
    mergesort(best_case)
    merge_end = timer()

    quick_worst_start = timer()
    quicksort(0, len(worst_case) - 1, worst_case)
    quick_worst_end = timer()

    merge_worst_start = timer()
    mergesort(worst_case)
    merge_worst_end = timer()

    return (
        timedelta(seconds=quick_end - quick_start),
        timedelta(seconds=merge_end - merge_start),
        timedelta(seconds=quick_worst_end - quick_worst_start),
        timedelta(seconds=merge_worst_end - merge_worst_start),
    )


if __name__ == "__main__":
    main()
