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

        # Change: geeft mee wat er verandert.
        # Kan meegegeven aan de ColDetect zodat deze de (illegale) movements ez kan terugdraaien
        change = []

        if action == 'down':
            change = [1, 0]

        # up: change rotation by 1
        elif action == 'up':
            self.currP.rotation = (self.currP.rotation + 1) % len(self.currP.shape)

        # left: position in width -1
        elif action == 'left':
            change = [0, -1]

        # right: position in width +1
        elif action == 'right':
            change = [0, 1]

        self.currP.changePosition(change[0], change[1])

        # TODO collisiondetection van blok met rechter en linker edge: naar links/ rechts bewegen van blok tot binnen de muren
        self.collDetect(change[0], change[1])

    def collDetect(self, x_changed, y_changed):
        block_positions = self.currP.get_positions()
        collision = False

        for row in range(len(self.positions)):
            for element in range(len(self.positions[0])):
                if self.positions(row, element) != 0:
                    if (row, element) in block_positions:
                        collision = True
                        break
            if collision:
                break

        for pos in block_positions:
            if pos[1] > len(self.positions[0]):
                # Todo Stuur hem naar het game-over screen, game is
                self.endGame()

        #Als de game niet over is, check dan of er lijnen zijn gemaakt
        self.removeLine()

        #Pak een nieuw blok klaar
        self.currP = self.nextP
        self.currP.makeCurrent()

        self.nextP = self.getRandomPiece()

    def removeLine(self, line):
        full = True
        for row in range(len(self.positions)):
            for element in range(len(self.positions[0])):
                if self.positions(row, element) != 0:
                    pass
                else:
                    full = False
            if full:
                np.delete(self.positions, row, 0)
                np.insert(self.positions, 0, np.zeros((1, len(self.positions[0]))), axis = 0)
            full = True
                
    def drawField(self):
        # canvas 2000x1200
        # plak erop u veld
        # rechts plak volgend stuk
        # onder rechts plak score
        pass

    def endGame(self):
        pass


class Piece:
    def __init__(self, shape):
        self.shape = shapes[shape]

        # Position = [x,y]
        self.position = [-1, -1]
        self.rotation = 0

    def makeCurrent(self):
        # Todo width bepalen
        width = 0
        self.position = [width/2, 0]

    def get_positions(self):
        positions = []

        for i in range(len(self.shape[self.rotation])):
            for j in range(len(self.shape[self.rotation][0])):
                if self.shape[self.rotation][i][j] == '0':
                    positions.append([self.position[0] + i - 2, self.position[1] + j - 2])
        return positions

    def changePosition(self, x, y):
        self.position = self.position[self.position[0] + x, self.position[1] + y]

    def set_positions(self, position):
        self.position = position
