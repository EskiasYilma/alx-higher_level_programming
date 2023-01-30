#!/usr/bin/python3
"""
Module Docstring
"""
import sys


def valid_move(board, row, col, n):
    """
    Check current position for previous incoming attacks
    """
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True


def nqueens(n):
    """
    Check current position for previous incoming attacks
    """
    if n < 4:
        print('N must be at least 4')
        return

    board = [-1] * n

    def bust_a_move(board, row):
        if row == n:
            move = []
            for i in range(n):
                move.append([i, board[i]])
            print(move)
            return

        for col in range(n):
            if valid_move(board, row, col, n):
                board[row] = col
                bust_a_move(board, row + 1)
    bust_a_move(board, 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    nqueens(int(sys.argv[1]))
