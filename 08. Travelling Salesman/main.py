from sys import maxsize
from itertools import permutations


def travellingSalesmanProblem(graph, s, v):
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    da_path = []
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        if min_path > current_pathweight:
            min_path = current_pathweight
            da_path = i

    return min_path, da_path


def main(graph, s, v):
    min_path, da_path = travellingSalesmanProblem(graph, s, v)
    da_path = [s, *da_path, s]
    da_path = [str(i + 1) for i in da_path]
    a = " ⇉ ".join(da_path)
    print(f"Minimum Path Length: {min_path}")
    print(f"Viable Path: {a}")


if __name__ == "__main__":
    s = 0
    # graph = [
    #     [0, maxsize, maxsize, 10, 20],
    #     [maxsize, 0, 50, 30, 40],
    #     [maxsize, 50, 0, maxsize, 60],
    #     [10, 30, maxsize, 0, maxsize],
    #     [20, 40, 60, maxsize, 0],
    # ]
    graph = [
        [0, 5, 5, 5, 25],
        [5, 0, 10, 5, 5],
        [5, 10, 0, 15, 5],
        [5, 5, 15, 0, 20],
        [25, 5, 5, 20, 0],
    ]
    v = 5
    main(graph, s, v)
