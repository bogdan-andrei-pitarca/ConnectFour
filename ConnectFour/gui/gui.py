import tkinter as tk
from tkinter import messagebox, simpledialog
from exceptions.errors import GameError
from game.game import Game
from players.human import HumanPlayer
from players.computer import AIPlayer

"""
this is the GUI class for my game
"""


class GUI:
    """ constructor, initializes everything """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self._game = Game()
        self.difficulty = self.choose_difficulty()
        self._ai = AIPlayer(self._game, difficulty=self.difficulty)
        self._human = HumanPlayer("Bogdan", self._game)
        self.chips = ["\U000026aa", "\U0001f534", "\U0001f7e1"]
        self.buttons = []
        self.labels = []
        self.create_widgets()

    def choose_difficulty(self):
        """
        choose easy, medium or hard difficulty (defaults to easy)
        """
        difficulty_levels = {"Easy": 1, "Medium": 2, "Hard": 3}
        choice = simpledialog.askstring("Difficulty", "Choose AI difficulty: Easy, Medium, or Hard")
        return difficulty_levels.get(choice, 1)
    def create_widgets(self):
        """
           used for creating the buttons, as well as the board
           """
        for col in range(7):
            button = tk.Button(self.root, text=f"↓", font=("Arial", 16), command=lambda c=col: self.player_move(c))
            button.grid(row=0, column=col, sticky="ew")
            self.buttons.append(button)

        for row in range(6):
            row_labels = []
            for col in range(7):
                label = tk.Label(self.root, text=self.chips[0], font=("Arial",24), width=3, height=1, borderwidth=2, relief="ridge")
                label.grid(row=row+1, column=col)
                row_labels.append(label)
            self.labels.append(row_labels)

    def update_board(self):
        """ updates the display based on the state """
        board = self._game.get_board()
        for row in range(6):
            for col in range(7):
                self.labels[row][col].config(text=self.chips[board[row][col]])

    def player_move(self, column):
        """ handles the player moves and checks for win conditions """
        try:
            self._human.make_move(column)
            self.update_board()
            if self._game.check_win(1):
                messagebox.showinfo("Game Over", "Player Wins!")
                self.root.quit()
                return

            self.computer_move()
        except GameError as e:
            messagebox.showerror("Invalid Move", str(e))


    def computer_move(self):
        """ handles the AI's moves and checks for win conditions """
        self._ai.make_move()
        self.update_board()
        if self._game.check_win(2):
            messagebox.showinfo("Game Over", "Computer Wins!")
            self.root.quit()
            return

        if self._game.check_full():
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.root.quit()
            return

    def run(self):
        """ runner function """
        self.root.mainloop()
