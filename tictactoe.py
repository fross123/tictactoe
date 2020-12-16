"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    # elif terminal(board):
    #     return "Game is over"
    else:
        # track moves so far
        count_x = 0
        count_o = 0
        for row in board:
            count_x += row.count(X)
            count_o += row.count(O)
        
        # return next player
        if count_x == count_o:
            return X
        elif count_x == count_o + 1:
            return O
        else:
            raise ValueError ("turn count is off.")

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # TODO:
    # if terminal(board):
    #     return "Terminal Board"

    # set of possible moves
    possible_moves = set()

    row_count = 0
    for row in board:
        row_count += 1
        for i in range(len(row)):
            if row[i] == None:
                action = (i, row_count)
                possible_moves.add(action)

    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
