import numpy as np
import random

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


class TetrisEnv:
    def __init__(self, height, width):
        self.positions = np.zeros((height, width))
        self.nextP = self.getRandomPiece()
        self.currP = self.getRandomPiece()
        self.currP.makeCurrent()
        self.score = 0

    def getRandomPiece(self):
        # pick a random shape from the shapes list
        return Piece(random.choice(shapes))

    def move(self, action):
        # action = string, {'down', 'up', 'left', right'}
        # down: position in height + 1
        if action == 'down':
            position = self.currP.get_positions()
            position[0] = position[0] + 1
            self.currP.set_positions(position)

        # up: change rotation by 1
        elif action == 'up':
            self.currP.rotation += 1

        # left: position in width -1
        elif action == 'left':
            position = self.currP.get_positions()
            position[1] = - 1
            self.currP.set_positions(position)

        # right: position in width +1
        elif action == 'right':
            position = self.currP.get_positions()
            position[1] = + 1
            self.currP.set_positions(position)

        # TO DO collisiondetection van blok met rechter en linker edge: naar links/ rechts bewegen van blok tot binnen de muren

    def collDetect(self):
        pass

    def removeLine(self, line):
        full = True
        for row in range(len(self.positions[0])):
            for element in range(len(self.positions[0])):
                if element != 0:
                    pass
                else:
                    full = False
            if full:
                np.delete(self.postions, row, 0)
                np.insert(self.postions, 0, np.zeros((1, len(self.positions[0]))), axis=0)
                
    def drawField(self):
        # canvas 2000x1200
        # plak erop u veld
        # rechts plak volgend stuk
        # onder rechts plak score
        pass


class Piece():
    def __init__(self, shape):
        self.shape = shapes[shape]
        self.position = [-1, -1]
        self.rotation = 0

    def makeCurrent(self):
        pass

    def get_positions(self):
        return self.position

    def set_positions(self, position):
        self.position = position
