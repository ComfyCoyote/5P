import random
from board import Board
class Player:
    def __init__(self, name, sign, board=None):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
        self.board = board

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self):
        valid_options = []
        for i in "ABCabc":
            for x in "123":
                valid_options.append(i + x)
        choosing = True
        while choosing:
            position_choice = input(f"{self.name} {self.sign}, Enter a cell [A-C][1-3] ")
            if position_choice not in valid_options:
                print("Invalid choice")
                choosing = True
            elif position_choice in valid_options:
                choosing = False
                valid_options.remove(position_choice)
                return position_choice.capitalize()


class SmartAI(Player, Board):
    def __init__(self, name, sign, board=None):
        super().__init__(name, sign, board)
        self.sign = sign
        self.board = board
        self. name = name

    def choose(self, board):
        # row win conditions
        ls = [0, 3, 6]
        xo = ["X","O"]
        for i in ls:
                if board[i] in xo and board[i] == board[i + 2] and board[i + 1] == " ":
                    return i + 1
                elif board[i] in xo and board[i] == board[i + 1] and board[i + 2] == " ":
                    return i + 2
                elif board[i + 1] in xo and board[i] == board[i + 2] and board[i] == " ":
                    return i
        # column win conditions
        lr = [0, 1, 2]
        for i in lr:
                if board[i] in xo and board[i] == board[i + 6] and board[i + 3] == " ":
                    return i + 3
                elif board[i] in xo and board[i] == board[i + 3] and board[i + 6] == " ":
                    return i + 6
                elif board[i + 3] in xo and board[i] == board[i + 6] and board[i] == " ":
                    return i
        # diagonal win conditions
        if board[0] in xo and board[0] == board[4] and board[8] == " ":
            return 8
        elif board[0] in xo and board[0] == board[8] and board[4] == " ":
            return 4
        elif board[8] in xo and board[8] == board[4] and board[0] == " ":
            return 0
        elif board[6] in xo and board[6] == board[4] and board[2] == " ":
            return 2
        elif board[4] in xo and board[4] == board[2] and board[6] == " ":
            return 6
        elif board[6] in xo and board[6] == board[2] and board[4] == " ":
            return 4
        elif board.count(" ") == 1:
            for i in range(9):
                if board[i] == " ":
                    return i
        else:
            x = random.randint(0, 9)
            if board[x] == " ":
                return x









