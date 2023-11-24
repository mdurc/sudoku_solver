# -*- coding: utf-8 -*-
"""
Author: Matthew Durcan

"""

def verify_board(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == ".":
                return "False, not solved"
            if not ok_to_add(r, c, board[r][c], board):
                return "False, not solved"
    return "True, is solved"


def is_valid_move(num, row, col, board):
    block = int(len(board) ** 0.5)
    for i in range(len(board)):
        row_contains_num = board[row][i] == num
        col_contains_num = board[i][col] == num
        
        #check the block now
        
        #row % block is the location of the row within the block it is in
        #row --- that location, gives the beginning of the block. And the i//block increments through the first second ... block rows and cols
        block_start_row = row - row % block + i // block
        block_start_col = col - col % block + i % block
        block_contains_num = board[block_start_row][block_start_col] == num
        
        if row_contains_num or col_contains_num or block_contains_num:
            return False
    return True


def solve_board(board):
    length = len(board)
    
    for r in range(length):
        for c in range(length):
            if board[r][c] == ".":
                for num in range(1, length+1):
                    if is_valid_move(str(num), r, c, board):
                        board[r][c] = str(num)
                        
                        temp_board = board.copy()
                        if solve_board(temp_board):
                            return temp_board
                        board[r][c] = "."
                return False
    return True



def ok_to_add(row, col, num, board):
    board[row][col] = "."
    if board[row].count(num)!=0:
        board[row][col]=num
        return False
    
    for r in range(len(board)):
        if board[r][col] == num:
            board[row][col]=num
            return False
    
    x = int(len(board)**0.5)
    
    gr = (row // x) * x
    gc = (col // x) * x
    
    for i in range(gr,gr+x):
        for j in range(gc,gc+x):
            if board[i][j] == num:
                board[row][col]=num
                return False
    
    board[row][col]=num
    return True


def reprint(board):
    x = int(len(board)**0.5)
    if x > 3:
        horiz = "-"*(x*(13)+1)
    else:
        horiz = "-"*31
    print(horiz)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if c%x==0:
                print("|", end="")
            if board[r][c] == ".":
                print(" . " , end="")
            else:
                print("{:2d} ".format(int(board[r][c])) , end="")
        if (r+1)%x==0:
            print("| ", horiz,sep="\n")
        else:
            print("| ")




def read_sudoku(filename):
    board = []
    for line in open(filename):
        line = line.strip("\n")
        board.append(line.split(" "))
    return board

files = ["easy1.txt", "easy2.txt", "medium.txt", "hard.txt"]


for f in files:
    print("\nFile name:",f)
    b = read_sudoku(f)

    print("Original:")
    reprint(b)
    solved_b = solve_board(b)

    print("Solved,",f, ":")
    reprint(solved_b)
