import tkinter as tk
from tkinter import messagebox

def isValid(sudoku, row, col, n):
    for i in range(9):
        if sudoku[row][i] == n or sudoku[i][col] == n:
            return False
    row_corner, col_corner = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[row_corner + i][col_corner + j] == n:
                return False
    return True

def solve(sudoku, row=0, col=0):
    if col == 9:
        col = 0
        row += 1
        if row == 9:
            return True
    if sudoku[row][col] > 0:
        return solve(sudoku, row, col + 1)
    for num in range(1, 10):
        if isValid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve(sudoku, row, col + 1):
                return True
            sudoku[row][col] = 0
    return False

def get_sudoku_from_gui():
    return [[int(entries[i][j].get() or "0") for j in range(9)] for i in range(9)]

def display_solution():
    sudoku = get_sudoku_from_gui()
    if solve(sudoku):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(sudoku[i][j]))
    else:
        messagebox.showerror("Error", "No solution exists!")

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[tk.Entry(root, width=3, font=('Arial', 14), justify="center") for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j, padx=2, pady=2)

solve_button = tk.Button(root, text="Solve", command=display_solution)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

root.mainloop()

