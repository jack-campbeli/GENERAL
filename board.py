import random

class Board:
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        self.winner = ""

    def get_size(self):
        return self.size

    def get_winner(self):
        return self.winner

    def set(self, index, sign):
        self.board[index] = sign

    def isempty(self,index):
        if self.board[index] == " ":
            return True
        else:
            return False

    def isdone(self):
        done = False
        if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != " ":
            self.winner = self.board[0]
            done = True
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != " ":
            self.winner = self.board[3]
            done = True
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != " ":
            self.winner = self.board[6]
            done = True
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != " ":
            self.winner = self.board[0]
            done = True
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != " ":
            self.winner = self.board[1]
            done = True
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != " ":
            self.winner = self.board[2]
            done = True
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != " ":
            self.winner = self.board[0]
            done = True
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != " ":
            self.winner = self.board[2]
            done = True
        else:
            if not " " in self.board:
                done = True
        return done

    def converttoIndex(self, pos):
        if pos == "A1":
            return 0
        elif pos == "B1":
            return 1
        elif pos == "C1":
            return 2
        elif pos == "A2":
            return 3
        elif pos == "B2":
            return 4
        elif pos == "C2":
            return 5
        elif pos == "A3":
            return 6
        elif pos == "B3":
            return 7
        elif pos == "C3":
            return 8
        else:
            return -1
        
    def chooseSmart(self, sign):
        opposite = 'X'
        if sign == 'X':
            opposite == 'O'
        elif sign == 'O':
            opposite == 'X'
        if self.board[5] == ' ':
            self.set(5, sign)
        elif ((self.board[0] == opposite and self.board[1] == opposite) or (self.board[0] == sign and self.board[1] == sign)) and (self.board[2] == ' '):
            self.set(2, sign)
        elif ((self.board[0] == opposite and self.board[2] == opposite) or (self.board[0] == sign and self.board[2] == sign)) and (self.board[1] == ' '):
            self.set(1, sign)
        elif ((self.board[1] == opposite and self.board[2] == opposite) or (self.board[1] == sign and self.board[2] == sign)) and (self.board[0] == ' '):
            self.set(0, sign)

        elif ((self.board[3] == opposite and self.board[4] == opposite) or (self.board[3] == sign and self.board[4] == sign)) and (self.board[5] == ' '):
            self.set(5, sign)
        elif ((self.board[3] == opposite and self.board[5] == opposite) or (self.board[3] == sign and self.board[5] == sign)) and (self.board[4] == ' '):
            self.set(4, sign)
        elif ((self.board[4] == opposite and self.board[5] == opposite) or (self.board[4] == sign and self.board[5] == sign)) and (self.board[3] == ' '):
            self.set(3, sign)

        elif ((self.board[6] == opposite and self.board[7] == opposite) or (self.board[6] == sign and self.board[7] == sign)) and (self.board[8] == ' '):
            self.set(8, sign)
        elif ((self.board[6] == opposite and self.board[8] == opposite) or (self.board[6] == sign and self.board[8] == sign)) and (self.board[7] == ' '):
            self.set(7, sign)
        elif ((self.board[7] == opposite and self.board[8] == opposite) or (self.board[7] == sign and self.board[8] == sign)) and (self.board[6] == ' '):
            self.set(6, sign)

        elif ((self.board[0] == opposite and self.board[3] == opposite) or (self.board[0] == sign and self.board[3] == sign)) and (self.board[6] == ' '):
            self.set(6, sign)
        elif ((self.board[0] == opposite and self.board[6] == opposite) or (self.board[0] == sign and self.board[6] == sign)) and (self.board[3] == ' '):
            self.set(3, sign)
        elif ((self.board[3] == opposite and self.board[6] == opposite) or (self.board[3] == sign and self.board[6] == sign)) and (self.board[0] == ' '):
            self.set(0, sign)

        elif ((self.board[1] == opposite and self.board[4] == opposite) or (self.board[1] == sign and self.board[4] == sign)) and (self.board[7] == ' '):
            self.set(7, sign)
        elif ((self.board[1] == opposite and self.board[7] == opposite) or (self.board[1] == sign and self.board[7] == sign)) and (self.board[4] == ' '):
            self.set(4, sign)
        elif ((self.board[4] == opposite and self.board[7] == opposite) or (self.board[4] == sign and self.board[7] == sign)) and (self.board[1] == ' '):
            self.set(1, sign)

        elif ((self.board[2] == opposite and self.board[5] == opposite) or (self.board[2] == sign and self.board[5] == sign)) and (self.board[8] == ' '):
            self.set(8, sign)
        elif ((self.board[2] == opposite and self.board[8] == opposite) or (self.board[2] == sign and self.board[8] == sign)) and (self.board[5] == ' '):
            self.set(5, sign)
        elif ((self.board[5] == opposite and self.board[8] == opposite) or (self.board[5] == sign and self.board[8] == sign)) and (self.board[2] == ' '):
            self.set(2, sign)

        elif ((self.board[0] == opposite and self.board[4] == opposite) or (self.board[0] == sign and self.board[4] == sign)) and (self.board[8] == ' '):
            self.set(8, sign)
        elif ((self.board[0] == opposite and self.board[8] == opposite) or (self.board[0] == sign and self.board[8] == sign)) and (self.board[4] == ' '):
            self.set(4, sign)
        elif ((self.board[4] == opposite and self.board[8] == opposite) or (self.board[4] == sign and self.board[8] == sign)) and (self.board[0] == ' '):
            self.set(0, sign)

        elif ((self.board[2] == opposite and self.board[4] == opposite) or (self.board[2] == sign and self.board[4] == sign)) and (self.board[6] == ' '):
            self.set(0, sign)
        elif ((self.board[2] == opposite and self.board[6] == opposite) or (self.board[2] == sign and self.board[6] == sign)) and (self.board[4] == ' '):
            self.set(0, sign)
        elif ((self.board[4] == opposite and self.board[6] == opposite) or (self.board[4] == sign and self.board[6] == sign)) and (self.board[2] == ' '):
            self.set(0, sign)

        else:
            choiceSmartAI = random.randint(0,8)
            while self.isempty(choiceSmartAI) == False:
                choiceSmartAI = random.randint(0,8)
            self.set(choiceSmartAI, sign)

    def show(self):
        print("\n    A   B   C")
        print("  +---+---+---+")
        print("1 | %s | %s | %s |" % (self.board[0], self.board[1], self.board[2]))
        print("  +---+---+---+")
        print("2 | %s | %s | %s |" % (self.board[3], self.board[4], self.board[5]))
        print("  +---+---+---+")
        print("3 | %s | %s | %s |" % (self.board[6], self.board[7], self.board[8]))
        print("  +---+---+---+")
