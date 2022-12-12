from rich.table import Table
from rich import print
from typing import List


class Node:
    def __init__(self, p, w) -> None:
        self.p = p
        self.w = w
        self.pbw = p / w
        self.x = 0

    def profit(self):
        return self.p * self.x

    def __repr__(self) -> str:
        return f"Profit: {self.p}; Weight: {self.w}; Profit by Weight: {self.pbw}; Portion: {self.x}"


def sorter(a):
    return sorted(a, key=lambda x: x.pbw)


def parts(M: int, w: int, wo: int):
    return (M - w) / wo


def print_result(arr: List):

    tb = Table()
    tb.add_column("Weight (W)")
    tb.add_column("Profit (P)")
    tb.add_column("Profit By Weight (P/W)")
    tb.add_column("Portion (X)")

    profit = 0
    for node in arr:
        tb.add_row(str(node.w), str(node.p), str(node.pbw), str(node.x))
        profit += node.profit()

    print(tb)

    print(f"Total profit: {profit}")


def main():

    n = int(input("Enter n: "))
    M = int(input("Enter M: "))

    done = False

    arr = []

    for i in range(0, n):
        inp = input().split()

        p, w = (int(i) for i in inp)
        arr.append(Node(p, w))

    arr = sorter(arr)
    arr.reverse()

    agg = 0
    for node in arr:
        if done == True:
            break

        if node.w >= M or node.w + agg >= M:
            node.x = parts(M, agg, node.w)
            break

        agg += node.w
        node.x = 1

    print_result(arr)


if __name__ == "__main__":
    main()
