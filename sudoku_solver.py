#sudoku solver
def isValid(sudoku,row,col,n):
    for i in range(9):
        if sudoku[row][i]==n:
            return False
        if sudoku[i][col]==n:
            return False
    row_corner=row-(row%3)
    col_corner=col-(col%3)
    for i in range(3):
        for j in range(3):
            if sudoku[row_corner+i][col_corner+j]==n:
                return False
    return True
def solve(sudoku,row,col):
    if col==9:
        if row==8:
            return True
        row+=1
        col=0
    if sudoku[row][col]>0:
        return solve(sudoku,row,col+1)
    for i in range(1,10):
        if isValid(sudoku,row,col,i):
            sudoku[row][col]=i
            if solve(sudoku,row,col+1):
                return True
        sudoku[row][col]=0
    return False
sudoku=[[0,0,0,0,0,0,6,8,0],
        [0,0,0,0,7,3,0,0,9],
        [3,0,9,0,0,0,0,4,5],
        [4,9,0,0,0,0,0,0,0],
        [8,0,3,0,5,0,9,0,2],
        [0,0,0,0,0,0,0,3,6],
        [9,6,0,0,0,0,3,0,8],
        [7,0,0,6,8,0,0,0,0],
        [0,2,8,0,0,0,0,0,0]]
if solve(sudoku,0,0):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print()
