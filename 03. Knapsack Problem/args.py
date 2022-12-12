from rich.table import Table
from rich import print as prt
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
    tb.add_column("[green]Weight (W)")
    tb.add_column("[green]Profit (P)")
    tb.add_column("[blue]Profit By Weight (P/W)")
    tb.add_column("[red]Portion (X)")

    profit = 0
    for node in arr:
        tb.add_row(str(node.w), str(node.p), str(node.pbw), str(node.x))
        profit += node.profit()

    prt(tb)

    prt(f"Total profit: [blue]{profit}")


def main(n: int, M: int, *args):

    done = False

    arr = []

    if len(args) == n:
        pass
    else:
        print("Invalid number of parameters")
        return

    for w, p in args:
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
    main(5, 20, (3, 10), (5, 20), (5, 21), (8, 30), (4, 16))
