
class HumanPlayer:
    def __init__(self, name, game):
        """
        constructor for the HumanPlayer class
        :param name: str
        :param game: Board
        """
        self._name = name
        self._board = game

    def make_move(self,val):
        """
        function that places a chip onto a certain column, chosen by the player
        :param val: int
        :return: -
        """
        self._board.make_move(val)

