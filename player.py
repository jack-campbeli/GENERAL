from board import Board
import random

class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name

    def choose(self, board):
        choice = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ").upper()
        choiceIndex = board.converttoIndex(choice)
        while (choiceIndex == -1) or (board.isempty(choiceIndex) == False):
            print("You did not choose correctly.")
            choice = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ").upper()
            choiceIndex = board.converttoIndex(choice)
        board.set(choiceIndex, self.sign)

class AI(Player):
    def choose(self, board):
        choiceAI = random.randint(0,8)
        while board.isempty(choiceAI) == False:
            choiceAI = random.randint(0,8)
        board.set(choiceAI, self.sign)

class SmartAI(Player):
    def choose(self, board):
        board.chooseSmart(self.sign)
