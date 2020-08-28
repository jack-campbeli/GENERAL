# assignment: programming assignment 5
# author: Jack Campbell
# date: 6-6-2020
# file: tictac.py acts as a tic-tac-toe board game.
# input: strings
# output: strings

from board import Board
from player import Player
from player import AI
from player import SmartAI

print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    player1 = AI("Bob", "X")
    player2 = SmartAI("Alice", "O")
    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")

    ans = input("Would you like to play again? [Y/N]").upper()
    if(ans != "Y"):
        break
print("Goodbye!")