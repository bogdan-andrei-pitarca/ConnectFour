from exceptions.errors import GameError
from game.game import Game
from players.human import HumanPlayer
from players.computer import AIPlayer
class UI:
    def __init__(self):
        self._game=Game()
        self._ai=AIPlayer(self._game)
        self._human=HumanPlayer("Bogdan", self._game)

    def print_board(self):
        board = self._game.get_board()
        for row in board:
            for column in row:
                print(f"{self.get_chip_symbol(column)}", end="")
            print()

    def get_chip_symbol(self, chip_value):
        chips = ["\U000026aa", "\U0001f534", "\U0001f7e1"]
        return chips[chip_value]

    def player_move(self):
        print("Player's turn!")
        column=int(input())
        try:
            self._human.make_move(column)
        except GameError as e:
            print(str(e))

    def computer_move(self):
        print("Computer's turn!")
        self._ai.make_move()

    def play(self):
        while self._game.game_over() is False:
            self.print_board()
            self.player_move()

            if self._game.check_win(1):
                self.print_board()
                print("Player Wins!")
                self._game.set_game_over(True)
                break

            self.print_board()
            self.computer_move()

            if self._game.check_win(2):
                self.print_board()
                print("Computer Wins!")
                self._game.set_game_over(True)
                break


            if self._game.check_full() is True:
                self.print_board()
                print("Draw!")
                self._game.set_game_over(True)
                break