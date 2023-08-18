"""
chessboard.py:
    list of lists representing a chessboard
"""

if __name__ == '__main__':
    EMPTY = ''
    ROOK = "ROOK"
    board = []

    for i in range(8):
        row = [EMPTY for i in range(8)]
        board.append(row)

    # board creation with list comprehension
    board = [[EMPTY for i in range(8)] for j in range(8)]

    board[0][0] = ROOK
    board[0][7] = ROOK
    board[7][0] = ROOK
    board[7][7] = ROOK

    print(board)
