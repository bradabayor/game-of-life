#!/usr/bin/env python
""" Generates a perpetual game of life. """

import time
from random import randrange

HEIGHT = 20
WIDTH = 40

def dead_state(height, width):
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
            line_list.append(0)
        board_list.append(line_list)
    return board_list

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

def next_board(current_board):
    new_board = dead_state(HEIGHT, WIDTH)
    neighbour_board = get_neighbours(current_board)
    for i, y in enumerate(neighbour_board):
        for j, x in enumerate(y):
            if x[0] == 0:
                new_board[i][j] = 1
            if x[0] == 1 & x[1] in range(0, 1):
                new_board[i][j] = 0
            if x[0] == 1 & x[1] in range(2, 3):
                new_board[i][j] = 0
            if x[0] == 1 & x[1] > 3:
                new_board[i][j] = 1
    return new_board
                
def get_neighbours(current_board):
    neighbour_board = dead_state(HEIGHT, WIDTH)
    for i, y in enumerate(current_board, start=0):
        for j, x in enumerate(y, start=0):
            neighbours = get_surrounds(i, j)
            total = check_neighbours(neighbours, board)
            neighbour_board[i][j] = [x, total]
    return neighbour_board

def check_neighbours(neighbours, current_board):
    alive_neighbours = 0
    for cell in neighbours:
        if current_board[cell[0]][cell[1]] == 1:
            alive_neighbours += 1
    return alive_neighbours
            
def get_surrounds(y, x):
    surrounds = []
    surrounds.append([y - 1, x - 1])
    surrounds.append([y - 1, x])
    surrounds.append([y - 1, x + 1])
    surrounds.append([y, x - 1])
    surrounds.append([y, x + 1])
    surrounds.append([y + 1, x - 1])
    surrounds.append([y + 1, x])
    surrounds.append([y + 1, x + 1])
    for cell in surrounds:
        if cell[0] < 0:
            cell[0] = HEIGHT - 1
        if cell[0] > HEIGHT - 1:
            cell[0] = 0
        if cell[1] < 0:
            cell[1] = WIDTH - 1
        if cell[1] > WIDTH - 1:
            cell[1] = 0
    return surrounds



board = random_state(HEIGHT, WIDTH)
render(board)

while True:
    board = next_board(board)
    render(board)
    time.sleep(0.2)
