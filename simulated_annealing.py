from abc import ABCMeta, abstractmethod
import random
import math
from ggplot import *
import pandas as pd
from board_base import BoardBase


class Board(BoardBase):
    def __init__(self):
        self.limit = 8
        self.board = [[None for y in xrange(self.limit)] for x in xrange(self.limit)]
        
        for row in self.board:
            row[random.randrange(self.limit)] = 1
     
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


    def get_board(self):
        return self.board

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
            row[random.randrange(self.limit)] = 1
        return board

    def improvise(self, board, limit = 1000, show = False):
        # Temperature is initialized to limit.
        temperature = limit
        heuristic = self.eval(board)
        final = heuristic
        costs = [heuristic]
        while True:
            if temperature == 0:
                if show:
                    print "Min heuristic cost attained:", final
                    data = pd.DataFrame({'Indices' : range(len(costs)), "Cost" : costs})
                    plt = ggplot(aes(x = 'Indices',y = 'Cost'), data = data) + \
                    geom_point()
                    plt.__repr__()
                return final

            # randomly select a neighbouring
            # state of board using the 
            # reservoir sampling method.
            next_move = self.reservoir_sampling(board)
            next_move_cost = self.eval(next_move)
            diff = next_move_cost - heuristic
            
            if diff > 0:
                board = next_move
                heuristic = next_move_cost
            else:
                prob_change = pow(math.e, float(diff) / temperature)
                rnd = random.random()
                if rnd < prob_change:
                    board = next_move
                    heuristic = next_move_cost
            temperature -= 1
            costs.append(heuristic)
            final = min(final, heuristic)


    def _clone_board(self, board):
        new_board = [[None for x in xrange(self.limit)] for y in xrange(self.limit)]
        for i in xrange(len(board)):
            for j in xrange(len(board)):
                new_board[i][j] = board[i][j]
        return new_board


    def reservoir_sampling(self, board, k = 1):
        index = 1
        answer = None
        for neighbour in self.next_moves(board):
            if answer == None:
                future_board, initial, future, new_cost = neighbour
                new_board = self._clone_board(board)
                new_board[initial[0]][initial[1]] = None
                new_board[future[0]][future[1]] = 1
                answer = new_board
                index += 1

            else:
                remember = 1.0 / index
                rnd_number = random.random()

                if rnd_number < remember:
                    future_board, initial, future, new_cost = neighbour
                    new_board = self._clone_board(board)
                    new_board[initial[0]][initial[1]] = None
                    new_board[future[0]][future[1]] = 1
                    answer = new_board
                index += 1
        return answer

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


b = Board()
print b.improvise(b.get_board(), show = True)