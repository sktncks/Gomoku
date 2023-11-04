import random

def get_ai_move(board, stone):
    """
    This function finds an empty spot on the board and returns the coordinates.
    :param board: The game board representation.
    :param stone: The stone color that the AI is using.
    :return: (x, y) tuple representing the coordinates where the AI will move.
    """
    empty_spots = [(x, y) for y in range(len(board)) for x in range(len(board[y])) if board[y][x] == 0]
    return random.choice(empty_spots) if empty_spots else None