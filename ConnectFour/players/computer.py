from exceptions.errors import GameError
import random
class AIPlayer:
    def __init__(self, game, difficulty=1):
        """
        constructor for the AIPlayer class
        :param game: Board
        """
        self._board = game
        self.difficulty = difficulty

    def make_move(self):
        """
        function that places a chip on the board, to the AI's liking (depending on the difficulty)
        :return: -
        """
        if self.difficulty == 1:
            self.easy_move()
        elif self.difficulty == 2:
            self.medium_move()
        else:
            self.hard_move()

    def easy_move(self):
        """
        the AI selects a random valid column
        :return: -
        """
        col = [column for column in range(7) if self._board.valid_move(column)]
        val = random.choice(col) if col else None
        if val is not None:
            self._board.make_move(val)

    def medium_move(self):
        """
        the AI blocks the player if they are about to win (besides that, the algorithm is random)
        :return: -
        """
        for col in range(7):
            if self._board.valid_move(col):
                self._board.make_move(col)
                if self._board.check_win(1):
                    self._board.undo_move(col)
                    self._board.make_move(col)
                    return
                self._board.undo_move(col)
        self.easy_move()


    def hard_move(self):
        """
        highest difficulty - AI makes a move based on a simple minimax algorithm
        :return:
        """
        best_score = float('-inf')
        best_col = None
        for col in range(7):
            if self._board.valid_move(col):
                self._board.make_move(col)
                score = self.minimax(3, False)
                self._board.undo_move(col)
                if score > best_score:
                    best_score = score
                    best_col = col

        if best_col is not None:
            self._board.make_move(best_col)
        else:
            self.easy_move()

    def minimax(self, depth, is_maximizing):
        """
        minimax algorithm with a depth limit
        :param depth: integer
        :param is_maximizing: boolean
        :return: min_eval, if is_maximizing is False, max_eval otherwise
        """
        if self._board.check_win(2):
            return 100
        if self._board.check_win(1):
            return -100
        if self._board.check_full() or depth == 0:
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for col in range(7):
                if self._board.valid_move(col):
                    self._board.make_move(col)
                    eval_score = self.minimax(depth - 1, False)
                    self._board.undo_move(col)
                    max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float('inf')
            for col in range(7):
                if self._board.valid_move(col):
                    self._board.make_move(col)
                    eval_score = self.minimax(depth - 1, True)
                    self._board.undo_move(col)
                    min_eval = min(min_eval, eval_score)
            return min_eval

