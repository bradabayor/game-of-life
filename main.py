#!/usr/bin/env python
""" Generates a perpetual game of life. """

from random import randrange

HEIGHT = 20
WIDTH = 40

def random_state(height, width):
    """random_state generates a board of size height x width, with a random
    starting value between 0 and 1.

    Args:
        height (int): height of the game board.
        width (int): width of the game board.

    Returns:
        list: two-dimensional list containings board starting values.
    """
    board_list = []
    for y in range(height):
        line_list = []
        for x in range(width):
            line_list.append(randrange(2))
        board_list.append(line_list)
    return board_list

def render(board):
    """render returns the game board output to the terminal.

    e.g (10 x 10):
    ------------
    |##   #####|
    |###  ##   |
    |#    ## ##|
    |#### #  # |
    |## #   # #|
    |###       |
    |     ##  #|
    | ### #   #|
    |#  #  ## #|
    |# #    # #|
    ------------

    Args:
        board (list): two-dimensional list of the current game borad state.
    """
    width = len(board[0])
    print('-' * (width + 2))
    for y in board:
        print('|', end='')
        for x in y:
            print(' ', end='') if x == 0 else print('#', end='')
        print('|')
    print('-' * (width + 2))


board = random_state(HEIGHT, WIDTH)
render(board)