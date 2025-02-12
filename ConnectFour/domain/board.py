import numpy as np
class Board:
    def __init__(self):
        """
        constructor for the Board; initializes a 6x7 matrix with 0
        """
        self._board=np.zeros((6,7),dtype=int)

    @property
    def board(self):
        """
        getter function for the board
        :return: matrix
        """
        return self._board