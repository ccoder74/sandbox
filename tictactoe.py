"""
tictatoe.py:
    - the computer (i.e., your program) should play the game using 'X's;
    - the user (e.g., you) should play the game using 'O's;
    - the first move belongs to the computer − it always puts its first 'X'
      in the middle of the board;
    - all the squares are numbered row by row starting with 1 (see the example
      session below for reference)
    - the user inputs their move by entering the number of the square they
      choose − the number must be valid, i.e., it must be an integer,
      it must be greater than 0 and less than 10, and it cannot point to a
      field which is already occupied;
    - the program checks if the game is over − there are four possible
      verdicts: the game should continue, the game ends with a tie, you win,
      or the computer wins;
    - the computer responds with its move and the check is repeated;
    - don't implement any form of artificial intelligence − a random field
      choice made by the computer is good enough for the game.
"""
from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


"""
def enter_move(board):
    # The function accepts the board's current status, asks the user about
    # their move, checks the input, and updates the board according to the
    # user's decision.


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and
    # column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if the player
    # using 'O's or 'X's has won the game.

"""
def draw_move(board):
    # The function draws the computer's move and updates the board.


if __name__ == '__main__':
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    draw_move(board)
