import numpy as np

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
shapes = [S, Z, I, O, J, L, T]

class TetrisEnv():
    def __init__(self,height, width):
        self.positions = np.zeros((height,width))
        self.nextP = self.getRandomPiece()
        self.currP = self.getRandomPiece()
        self.currP.makeCurrent()
        self.score = 0


    def getRandomPiece(self):
        return Piece(1)

    def move(self, action):
        pass

    def collDetect(self):
        pass

    def removeLine(self, line):
        pass

    def drawField(self):
        #canvas 2000x1200
        #plak erop u veld
        #rechts plak volgend stuk
        #onder rechts plak score
        pass


class Piece():
    def __init__(self, shape):
        self.shape = shapes[shape]
        self.position = (-1, -1)
        self.rotation = 0

    def makeCurrent(self):
        pass

    def get_positions(self):
        pass