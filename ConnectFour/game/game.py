from domain.board import Board
from exceptions.errors import GameError
import numpy as np
class Game:
    def __init__(self):
        """
        constructor for the Game class
        """
        self._board=Board()
        self._gameover=False
        self._player=0

    def switch_player(self):
        """
        function that switches between player 0 (human) and player 1 (computer)
        :return: -
        """
        self._player=self._player^1

    def get_player(self):
        """
        getter function for the player
        :return: int
        """
        return self._player

    def set_game_over(self,TF: bool):
        """
        setter function for gameover
        :param TF: bool
        :return: -
        """
        self._gameover=TF

    def game_over(self):
        """
        getter function for gameover
        :return: True / False
        """
        return self._gameover

    def valid_row(self,column):
        """
        function that determines the valid placement of a chip on the board, in regard to its column
        :param column: int,
        :return: int,
        :raises: GameError, if the move is invalid
        """
        if self.valid_move(column) is False:
            raise GameError("Can't place that there!")
        else:
            for row in range(6):
                if self._board.board[row][column] == 0:
                    return row
            return 6
    def make_move(self,column):
        """
        function that "places" a chip on the board (cells marked with 1 will equal chips placed by player, those marked with 2 = chips placed by computer)
        :param column: int
        :return: -
        """
        self._board.board[self.valid_row(column)][column]=self.get_player()+1
        self.switch_player()

    def undo_move(self, column):
        """
        function that undoes the last move in the given column by resetting the top-most non-empty cell
        :param column: int
        :raises: GameError, if the column is already empty
        """
        for row in range(5, -1, -1):
            if self._board.board[row][column] != 0:
                self._board.board[row][column] = 0
                self.switch_player()
                return
        raise GameError("No moves to undo in this column.")

    def valid_move(self,column):
        """
        function that determines whether a move is valid or not
        :param column: int
        :return: True / False
        """
        if column < 0 or column > 6 or self._board.board[5][column] == 1 or self._board.board[5][column] == 2:
            return False
        return True

    def check_full(self):
        """
        function that checks whether the board is full or not
        :return: True / False
        """
        c=0
        for column in range(7):
            for row in range(6):
                if self._board.board[row][column] == 0:
                    c += 1
        if c == 0:
            return True
        return False

    def check_win(self,player):
        """
        function that checks whether the game has been won or not
        :param player: int
        :return: True / False
        """
        for row in range(6):
            for column in range(4):
                if all(self._board.board[row,column+i]==player for i in range(4)):
                    return True
        for column in range(7):
            for row in range(3):
                if all(self._board.board[row+i,column]==player for i in range(4)):
                    return True

        for row in range(3):
            for column in range(4):
                if all(self._board.board[row+i,column+i]==player for i in range(4)):
                    return True

        for row in range(2,6):
            for column in range(4):
                if all(self._board.board[row-i,column+i]==player for i in range(4)):
                    return True

        return False

    def get_board(self):
        """
        getter for the board, flipped for a correct display
        :return: Board
        """
        return np.flip(self._board.board,0)

