# author: Muzzammil Adamjee
# date: December 5, 2021
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: The program requests user input regarding which cell they would like to place a designated marker in.
# It is designed for two players and requests inputs from each respectively.
# output: After receiving the inputs, the program prints the tic tac toe board with the assigned symbol in the chosen
# square. This is repeated until there is a winner, whence the program outputs the declaration of victory and
# requests confirmation for another game


from player import Player
from board import Board
tictac = True
while tictac:
    print("Welcome to Tic Tac Toe!")
    board = Board()
    player1 = Player("Bob", "X")
    player2 = Player("Alice", "O")
    board.show()

    playing = True
    while playing:

        board._set(board.isempty(player1.choose(), player1),"X")
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
        playing = False
        print("Goodbye!")
