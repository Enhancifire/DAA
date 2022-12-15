"""Assignment 06: N Queens Problem:main.py"""
import gui

global N


def print_sol(board):
    for i in range(N):
        print(" | ".join([str(j) for j in board[i]]))


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_N_Queens(board, col):

    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_N_Queens(board, col + 1):
                return True

            board[i][col] = 0
    return False


def main():
    global N
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve_N_Queens(board, 0):
        print(f"Solution for {N}X{N} Queens Problem:")
        print_sol(board)
        gui.create_GUI(board, N)
    else:
        print("No Solution found")


if __name__ == "__main__":
    global N
    N = int(input("Enter N: "))
    main()
