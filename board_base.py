from abc import ABCMeta, abstractmethod

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