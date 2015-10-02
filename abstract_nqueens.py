from abc import ABCMeta, abstractmethod
import random
import math
from ggplot import *
import pandas as pd

class BoardBase(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def next_moves(self, board):
        pass

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def improvise(self):
        pass

class Board(BoardBase):
    def __init__(self):
        self.limit = 8
        self.board = [[None for y in xrange(self.limit)] for x in xrange(self.limit)]
        
        for row in self.board:
            row[random.randrange(8)] = 1
     
        self.moves = [
        lambda x, y : (x, y + 1),
        lambda x, y : (x + 1, y + 1),
        lambda x, y : (x + 1, y),
        lambda x, y : (x + 1, y - 1),
        lambda x, y : (x, y - 1),
        lambda x, y : (x - 1, y - 1),
        lambda x, y : (x - 1, y),
        lambda x, y : (x - 1, y + 1)
        ]
        
    def __str__(self):
        return self._print_board(self.board)

    def next_moves(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if board[i][j] == 1:
                    ctr = 0
                    for move in self.moves:
                        x, y = move(i, j)
                        ctr += 1
                        if self._is_valid(x, y) and board[x][y] == None:
                            board[i][j] = None
                            board[x][y] = 1
                            yield (board, (i, j), (x, y), self.eval(board))
                            board[x][y] = None
                            board[i][j] = 1

    def _print_board(self, board):
        answer = [" ".join(map(lambda x : "Q" if x else ".", row)) for row in board]
        return "\n".join(answer)



    def _randomize(self, board):
        board = [[None for y in xrange(self.limit)] for x in xrange(self.limit)]
        for row in board:
            row[random.randrange(8)] = 1
        return board

    def improvise(self, limit = 100, random_restart = False, restart_probability = 0.5, show = False):
        costs = []
        self.board = self._randomize(self.board)
        heuristic_cost = self.eval(self.board)
        iterations = 0
        costs.append(heuristic_cost)
        while iterations < limit:

            if random_restart:
                random_value = random.random()
                if random_value <= restart_probability:
                    self.board = self._randomize(self.board)
                    heuristic_cost = self.eval(self.board)

            iterations += 1
            if heuristic_cost == 0:
                return 0
            
            curr_cost = heuristic_cost
            initial_f = None
            future_f = None

            for next_config in self.next_moves(self.board):
                future_board, initial, future, new_cost = next_config
                if new_cost < curr_cost:
                    curr_cost = new_cost
                    initial_f = initial
                    future_f = future

            if initial_f != None:
                self.board[initial_f[0]][initial_f[1]] = None
                self.board[future_f[0]][future_f[1]] = 1
            heuristic_cost = curr_cost
            costs.append(heuristic_cost)
        
        if show:
            print "Min heuristic cost attained:", min(costs)
            print self
        
            data = pd.DataFrame({'Indices' : range(len(costs)), "Cost" : costs})
            plt = ggplot(aes(x = 'Indices',y = 'Cost'), data = data) + \
            geom_point()
            plt.__repr__()

        return min(costs)

    def _is_valid(self, x, y):
        return 0 <= x < self.limit and 0 <= y < self.limit

    def _iter(self, x, y, move, board):
        x, y = move(x, y)
        while self._is_valid(x, y):
            if board[x][y] == 1:
                return 1
            x, y = move(x, y)
        return 0

    def eval(self, board):
        total = 0
        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if board[i][j] == 1:
                    # there is a queen here.
                    for move in self.moves:
                        total += self._iter(i, j, move, board)
        return total / 2
