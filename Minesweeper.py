import random


class Tile:
    def __init__(self, bomb=False):
        self.bomb = bomb
        self.numNeighbors = 0
        self.revealed = False
        self.flagged = False
        self.uncovered = False

    def isBomb(self):
        return self.bomb
    
    def setNumNeighbors(self,numNeighbors):
        self.numNeighbors = numNeighbors

    def flag(self):
        if self.uncovered:
            return
        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True
    
    def reveal(self):
        if(self.flagged):
            print("Cannot reveal a flagged tile - please unflag first")
            return -1
        self.uncovered = True
        if self.bomb:
            return 1
        else:
            return 0
        return self.bomb

    def print(self):
        if self.flagged:
            print("F",end=' | ')
        elif self.uncovered:
            print(self.numNeighbors,end=' | ')
        else:
            print(" ", end=' | ')

class Board:
    def __init__(self, size=10, numBombs=20):
        self.size = size
        self.numBombs = numBombs
        self.tilesCovered = size*size
        bombsRemaining = numBombs
        tilesRemaining = size*size
        self.tiles = []
        for i in range(size):
            row = []
            for j in range(size):
                isbomb = random.random() < (bombsRemaining / tilesRemaining)
                row.append(Tile(isbomb))
            self.tiles.append(row)

        for i in range(size):
            for j in range(size):
                numNeighbors = 0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if x == 0 and y == 0:
                            continue
                        if self.coordInRange(i+x,j+y):
                            if self.tiles[i+x][j+y].isBomb():
                                numNeighbors += 1
                self.tiles[i][j].setNumNeighbors(numNeighbors)

    def print(self):
        for i in range(self.size):
            # print("__ "*(self.size+2))
            print("| ", end='')
            for j in range(self.size):
                self.tiles[i][j].print()
            print()
        # print("__"*(self.size+2))

    def coordInRange(self, x, y):
        if x >= 0 and y >= 0 and x < self.size and y < self.size:
            return True
        return False

    def flag(self, x, y):
        if self.coordInRange(x,y):
            self.tiles[x][y].flag()
        else:
            print("Coords", x, ",",y,"are not in the board")

    def reveal(self,x,y):
        if self.coordInRange(x,y):
            ret = self.tiles[x][y].reveal()
            if ret == 0:
                self.tilesCovered -= 1
                return False
            elif ret == 1:
                print("You uncovered a bomb - Game Over!")
                return True                
        else:
            print("Coords", x, ",",y,"are not in the board")
        return False

class Game:
    def __init__(self, size=10,numBombs = 20):
        self.board = Board(size,numBombs)

    def playRound(self):
        print("Current Board: ")
        self.board.print()
        print()
        if(self.board.tilesCovered == self.board.numBombs):
            print("Congrats - you win!!!!")
            return True
        inp = input("Enter your move> ").split(' ')
        if len(inp) != 3:
            print("Move should be of type: [F(lag) OR C(lick)] X Y")
            return False
        else:
            if inp[0] == 'F' or inp[0] == 'f':
                self.board.flag(int(inp[1]),int(inp[2]))
                return False
            elif inp[0] == 'C' or inp[0] == 'c':
                return self.board.reveal(int(inp[1]),int(inp[2]))
            else:
                print("The first input should be either F or C (for Flag and Click)")
                return False

while(True):
    inp = input("Please enter the size of the board (length of one side) and number of bombs as a tuple separated by space (ie: # #): ").split(' ')
    if len(inp) != 2:
        print("Incorrect input - should be: # #")
    else:
        break
g = Game(int(inp[0]),int(inp[1]))
while(True):
    if g.playRound():
        break
