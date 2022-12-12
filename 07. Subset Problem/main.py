"""Assignment 7 Subset Sum Problem: main.py"""


def calculate(num_set, req_sum):
    """Calculates the solution
    Takes set of numbers and required sum as parameters
    """
    sublists = get_sublists(num_set)
    solutionLists = []
    solutions = 0
    for i in sublists:
        if sum(i) == req_sum:
            solutions += 1
            solutionLists.append(i)

    return solutionLists, solutions


def get_sublists(num_set):
    """Returns a list of Sublists from given list parameter"""
    from itertools import combinations

    lists = []
    for i in range(len(num_set) + 1):
        lists += [list(j) for j in combinations(num_set, i)]

    return lists


def main():
    """Main Function of the Program"""
    numset = input("Enter the elements: ").split()
    numset = [int(i) for i in numset]

    req_sum = int(input("Sum required: "))

    solutionsLists, solutions = calculate(numset, req_sum)
    print(f"Number of Solutions available are: {solutions}")
    print(f"Solution Subsets are: {solutionsLists}")


if __name__ == "__main__":
    main()
