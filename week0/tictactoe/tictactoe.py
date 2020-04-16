"""
Tic Tac Toe Player
"""

import math
from random import randint

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
    Returns player who has the next turn on a board (either X or O).
    
    In the initial game state, X gets the first move.
    Subsequently, the player alternates with each additional move.
    
    Any return value is acceptable if a terminal board is provided as input 
    (i.e., the game is already over).
    """
    count = 0
    
    for row in board:
        for i in row:
            if i is not EMPTY:
                count += 1
    
    if count % 2 == 0:
        return(X)
    else:
        return(O)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    where i corresponds to the row of the move (0, 1, or 2)
    j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    
    Possible moves are any cells on the board 
    that do not already have an X or an O in them.
    
    Any return value is acceptable if a terminal board is provided as input.
    """
    
    actions = []
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col is EMPTY:
                actions.append((i, j))
    
    return(set(actions))
                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    
    If action is not a valid action for the board, your program should raise an exception.
    
    The returned board state should be the board 
    that would result from taking the original input board, 
    and letting the player whose turn it is make their move 
    at the cell indicated by the input action.
    
    Importantly, the original board should be left unmodified
    """
    val = player(board)
    new_board = board.copy()
    
    new_board[action[0]][action[1]] = val
    
    return(new_board)
    
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    If the X player has won the game, your function should return X. 
    If the O player has won the game, your function should return O.
    
    If there is no winner of the game 
    (either because the game is in progress, or because it ended in a tie), 
    the function should return None.
    """
    
    # return None if game still in progress
    if not terminal(board):
        return(None)
    
    col0 = []
    col1 = []
    col2 = []    
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == O:
                return(O)
            elif row[0] == X:
                return(X)
        col0.append(row[0])
        col1.append(row[1])
        col2.append(row[2])
    
    if col0[0] == col0[1] == col0[2] == O:
        return(O)
    elif col0[0] == col0[1] == col0[2] == X:
        return(X)
            
    elif col1[0] == col1[1] == col1[2] == O:
        return(O)
    elif col1[0] == col1[1] == col1[2] == X:
        return(X)
            
    elif col2[0] == col2[1] == col2[2] == O:
        return(O)
    elif col2[0] == col2[1] == col2[2] == X:
        return(X)

    if col0[0] == col1[1] == col2[2] == O:
        return(O)
    elif col0[0] == col1[1] == col2[2] == X:
        return(X)
    elif col2[0] == col1[1] == col0[2] == O:
        return(O)
    elif col2[0] == col1[1] == col0[2] == X:
        return(X)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    all_vals = []
    col0 = []
    col1 = []
    col2 = []
    for row in board:
        for i in row:
            all_vals.append(i)
        # check for horizontal 3 in a rows
        if row[0] == row[1] == row[2]:
            if any(i is None for i in row):
                return(False)
            return(True)
    # check for vertical 3 in a rows
        col0.append(row[0])
        col1.append(row[1])
        col2.append(row[2])
    if col0[0] == col0[1] == col0[2]:
        if any(i is None for i in col0):
                return(False)
        return(True)
    elif col1[0] == col1[1] == col1[2]:
        if any(i is None for i in col1):
                return(False)
        return(True)
    elif col2[0] == col2[1] == col2[2]:
        if any(i is None for i in col2):
                return(False)
        return(True)
    
    # check for diagonals
    if col0[0] == col1[1] == col2[2]:
        return(True)
    elif col2[0] == col1[1] == col0[2]:
        return(True)
    
    # check if board is filled    
    if None not in all_vals:
        return(True)
    
    return(False)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    utility will only be called on a board if terminal(board) is True
    """
    
    if winner(board) == O:
        return(-1)
    elif winner(board) == X:
        return(1)
    else:
        return(0)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    The move returned should be the optimal action (i, j)
    that is one of the allowable actions on the board.
    
    If multiple moves are equally optimal, any of those moves is acceptable.
    
    If the board is a terminal board, the minimax function should return None.
    """
    if terminal(board):
        return(None)
    
    current_player = player(board)
    
    possible_actions = actions(board)
    
    if current_player == X: # want to max out
        pass
    
    for i, action in enumerate(possible_actions):
        pass
    
    
    # for now
    return(list(possible_actions)[randint(0, len(possible_actions)-1)])    
    

if __name__ == "__main__":
    
    board = [[X, EMPTY, X],
             [X, O, X],
             [O, O, X]]
    
    print(player(board))