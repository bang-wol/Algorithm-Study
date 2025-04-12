import sys
import copy
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_block = 0

def move_left(board):
    new_board = []
    for row in board:
        new_row = []
        last = None
        for num in row:
            if num == 0:
                continue
            if last is None:
                last = num
            elif last == num:
                new_row.append(last*2)
                last = None
            else:
                new_row.append(last)
                last=num
        if last is not None:
            new_row.append(last)
        new_row += [0] * (len(board) - len(new_row))
        new_board.append(new_row)
        
    return new_board

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    moved = move_left(reversed_board)
    
    return [row[::-1] for row in moved]

def rotate(board):
    return [list(row) for row in zip(*board[::-1])]

def rotate_back(board):
    return [list(row) for row in zip(*board)][::-1]

def move_up(board):
    rotated = rotate(board)
    moved = move_left(rotated)
    
    return rotate_back(moved)

def move_down(board):
    rotated = rotate(board)
    moved = move_right(rotated)
    
    return rotate_back(moved)

def dfs(board, depth):
    global max_block

    for row in board:
        max_block = max(max_block, max(row))
    if depth == 5:
        return 
    
    for move_function in [move_left, move_right, move_up, move_down]:
        moved_board = move_function(copy.deepcopy(board))
        if moved_board != board:
            dfs(moved_board, depth + 1)
            
dfs(board, 0)
print(max_block)