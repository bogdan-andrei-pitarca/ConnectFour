from game.game import Game
from players.human import HumanPlayer
from players.computer import AIPlayer
import unittest

class GameTests(unittest.TestCase):
    def setUp(self):
        self._game=Game()

    def test_switch_player(self):
        initial = self._game.get_player()
        self._game.switch_player()
        new = self._game.get_player()
        self.assertNotEqual(initial, new)
        self.assertIn(new,[0,1])
        self.assertEqual(new,initial^1)

    def test_make_move(self):
        initial = self._game.get_board().copy()
        self._game.make_move(0)
        self.assertEqual(self._game.get_board()[5,0],1)
        self.assertNotEqual(self._game.get_player(),0)
        self.assertFalse((self._game.get_board()==initial).all())

    def test_valid_move(self):
        valid = 2
        invalid = 9
        self.assertTrue(self._game.valid_move(valid))
        self.assertFalse(self._game.valid_move(invalid))

    def test_check_full(self):
        self.assertFalse(self._game.check_full())
        for column in range(7):
            for row in range(6):
                self._game.make_move(column)
        self.assertTrue(self._game.check_full())

    def test_get_board(self):
            flipped = self._game.get_board()
            self.assertTrue((flipped == self._game._board.board[::-1]).all())


if __name__ == '__main__':
    unittest.main()