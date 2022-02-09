dic1 = {"A1": 0, "A2": 3, "A3": 6, "B1": 1, "B2": 4, "B3": 7, "C1": 2, "C2": 5, "C3": 8}


class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign O or X
        self.winner = ""
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def get_size(self):
        # optional, return the board size (an instance size
        return self.size

    def get_winner(self, sign):
        # return the winner's sign O or X (an instance winner)
        if sign == "X" or sign == "O":
            print(f"{sign} is the winner!")
            return sign
        elif sign == "haha":
            print("Its a tie!")

    def get_board(self):
        print(self.board)

    def _set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) or a dictionary to obtain indexes
        # this implementation is up to you

        if cell in dic1:
            y = dic1.get(cell)
            self.board[y] = sign
        else:
            self.board[cell] = sign

    def isempty(self, cell, player):

        y = dic1.get(cell)
        if self.board[y] == " ":
            return cell
        else:
            print("The cell is occupied, try again ")
            player.choose()


    def isdone(self):
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        xo = ["X", "O"]
        ls = [0, 3, 6]
        for i in ls:
            if self.board[i] in xo and self.board[i] == self.board[i + 1] == self.board[i + 2]:
                return self.board[i]
        lr = [0, 1, 2]
        for i in lr:
            if self.board[i] in xo and self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return self.board[i]
        if self.board[0] in xo and self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]

        elif self.board[6] in xo and self.board[6] == self.board[4] == self.board[2]:
            return self.board[6]
        elif " " not in self.board:
            return "haha"

    def show(self):
        # draw the board
        board = self.board
        letter = "   A   B   C  "
        divider = " +---+---+---+"
        row1 = "1|" + board[0] + "  |" + board[1] + "  |" + board[2] + "  |"
        row2 = "2|" + board[3] + "  |" + board[4] + "  |" + board[5] + "  |"
        row3 = "3|" + board[6] + "  |" + board[7] + "  |" + board[8] + "  |"
        print(letter)
        print(divider)
        print(row1)
        print(divider)
        print(row2)
        print(divider)
        print(row3)
        print(divider)
