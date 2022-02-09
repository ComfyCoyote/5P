# author: Muzzammil Adamjee
# date: December 5, 2021
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: The program requests user input regarding which cell they would like to place a designated marker in. Unlike
# the standard tic tac toe, which is played between two humans, this program places an AI against a human.
# output: The game begins with the computer taking the first turn.
# After receiving user input the program prints the tic tac toe board with the assigned symbol in the chosen
# square. This is repeated until there is a winner, whence the program outputs the declaration of victory and
# requests confirmation for another game.




from player import Player, SmartAI
from board import Board



tictac = True
while tictac:
    board = Board()
    player1 = SmartAI("Bob", "X")
    player2 = Player("Alice", "O")
    print("Welcome to AI Tic Tac Toe")
    playing = True
    while playing:
        board._set(player1.chooseALT(board.board),"X")
        board.show()
        if board.isdone() == "X" or board.isdone() == "O":
            playing = False
            board.get_winner(board.isdone())
            break
        board._set(board.isempty(player2.choose(), player2), "O")
        board.show()
        if board.isdone() == "X" or board.isdone() == "O":
            playing = False
            board.get_winner(board.isdone())
            break
    again = input("Would you like to play again [Y/N]? ")
    if again == "Y":
        tictac = True
    elif again == "N":
        tictac = False
        print("Goodbye!")

