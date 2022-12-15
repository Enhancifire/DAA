"""Assignment 5 0/1 Knapsack: main.py"""
import dp
import backtrack
import branchandbound


def main(n, w, elems):
    """Main Driver Function of All 3 Algorithms"""

    dpans = dp.knapsack(n, elems, w)
    val = elems[0]
    wt = elems[1]
    backans = backtrack.knapsack(w, wt, val, n)
    branchandbound.knapsack(n, elems, w)

    print()
    print(f"DP Ans: {dpans}")
    print(f"BackTrack Ans: {backans}")


# if __name__ == "__main__":
#     n = int(input("Number of Elements: "))
#     w = int(input("Enter max weight: "))
#     elems = [[], []]
#     print("Enter elements value and weight")
#     for i in range(n):
#         a, b = input(f"Enter element {i + 1}: ").split()
#         elems[0].append(int(a))
#         elems[1].append(int(b))
#     main(n, w, elems)


if __name__ == "__main__":
    n = 5
    w = 20
    elems = [[10, 20, 21, 30, 16], [3, 5, 5, 8, 4]]
    main(n, w, elems)
