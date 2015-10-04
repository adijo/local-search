"""
Hill climbing.
"""

from abstract_nqueens import Board

board = Board()
board.improvise(board.get_board(), limit = 100, show = True)
