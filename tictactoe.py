"""
Tic Tac Toe Player
"""

import math
import copy
import numpy

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
    elif terminal(board):
        return "Game is over"
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

    # set of possible moves
    possible_moves = set()
    
    row_count = 0
    for row in board:
        for i in range(len(row)):
            if row[i] == None:
                action = (row_count, i)
                possible_moves.add(action)
        row_count += 1

    # check if there are any possible moves
    if len(possible_moves) == 0:
        return None
    else:
        return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if terminal(board):
        raise ValueError("Terminal board")
    elif action not in actions(board):
        raise ValueError("Action not possible")
    else:
        cp_board = copy.deepcopy(board)
        cp_board[action[0]][action[1]] = player(cp_board)
        return cp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Row winner
    for row in board:
        if len(set(row)) == 1 and row[0] != None:
            return row[0]
    
    # Column winner
    for rev_board in [board, numpy.transpose(board)]:
        for row in rev_board:
            if len(set(row)) == 1 and row[0] != None:
                return row[0]
    
    # Diagonal winner
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]

    return None    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif actions(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    else:
        if player(board) == X:
            high_value = -math.inf
            for action in actions(board):
                v = min_value(result(board, action))
                if v > high_value:
                    high_value = v
                    best_action = action
            # print(f"X moves: {best_action}")
            return best_action
            
        elif player(board) == O:
            low_value = math.inf
            for action in actions(board):
                v = max_value(result(board, action))
                if v < low_value:
                    low_value = v
                    best_action = action
            # print(f"O moves: {best_action}")
            return best_action


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
