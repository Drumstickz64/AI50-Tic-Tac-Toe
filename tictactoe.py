"""
Tic Tac Toe Player
"""

from copy import deepcopy
import sys

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if cell == EMPTY:
                action_list.append((i, j))

    return action_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    (i, j) = action
    if i < -3 or i > 2:
        raise IndexError(f"row index out of bounds: i = {i}, rows = 3")

    if j < -3 or j > 2:
        raise IndexError(f"column index out of bounds: j = {i}, columns = 3")

    if board[i][j] != EMPTY:
        raise InvalidActionError(
            f"move at row ({i}), column ({j}) is not an empty cell"
        )

    new_board = deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


class InvalidActionError(Exception):
    ...


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    match utility(board):
        case 1:
            return X
        case -1:
            return O
        case _:
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return len(actions(board)) == 0 or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for player, util in ((X, 1), (O, -1)):
        # Check rows
        for row in board:
            if row.count(player) == 3:
                return util

        # Check columns
        for j in range(3):
            col = [board[i][j] for i in range(3)]
            if col.count(player) == 3:
                return util

        # Check diagonals
        diag1 = [board[i][i] for i in range(3)]
        diag2 = [board[i][2 - i] for i in range(3)]
        if diag1.count(player) == 3:
            return util
        if diag2.count(player) == 3:
            return util

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return find_optimal_maximizer_move(board)

    return find_optimal_minimizer_move(board)


def find_optimal_maximizer_move(board):
    best_move = None
    best_score = -2
    for move in actions(board):
        score = min_value(result(board, move))
        # move with a score of 1 is already ideal
        if score == 1:
            return move

        if score > best_score:
            best_move = move
            best_score = score

    return best_move


def find_optimal_minimizer_move(board):
    best_move = None
    best_score = 2
    for move in actions(board):
        score = max_value(result(board, move))
        # move with a score of -1 is already ideal
        if score == -1:
            return move

        if score < best_score:
            best_move = move
            best_score = score

    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)

    value = -2
    for move in actions(board):
        score = min_value(result(board, move))
        # found highest possible score
        if score == 1:
            return 1
        value = max(value, score)

    return value


def min_value(board):
    if terminal(board):
        return utility(board)

    value = 2
    for move in actions(board):
        score = max_value(result(board, move))
        # found lowest possible score
        if score == -1:
            return -1
        value = min(value, score)

    return value
