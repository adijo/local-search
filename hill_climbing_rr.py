"""
Hill climbing with random restart.
"""

from abstract_nqueens import Board
board = Board()
print board.improvise(board.get_board(), show = True, limit = 1000, random_restart = True, restart_probability = 0.3)
