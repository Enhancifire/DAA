import tkinter
from tkinter import Button


def create_GUI(board, N):
    root = tkinter.Tk()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bg = "#A1EF8B"
            else:
                bg = "#92D5E6"
            Button(root, padx=20, pady=20, bg=bg).grid(
                column=j,
                row=i,
            )
    root.mainloop()
