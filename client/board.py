def board():
    row, col = 8, 8

    board = [[""]*col]*row

    return board

def printBoard(board):
    for rows in board:
        print(rows)


pp = board()

printBoard(pp)
