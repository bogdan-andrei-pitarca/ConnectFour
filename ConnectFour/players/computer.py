from exceptions.errors import GameError
import random
class AIPlayer:
    def __init__(self, game):
        """
        constructor for the AIPlayer class
        :param game: Board
        """
        self._board = game

    def make_move(self):
        """
        function that places a chip on the board, to the AI's liking
        :return: -, None if no valid moves are available
        """
        col = [column for column in range(7) if self._board.valid_move(column)]
        val = random.choice(col) if col else None
        if val is not None:
            self._board.make_move(val)

