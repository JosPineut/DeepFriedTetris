import numpy as np
import random
import pygame

pygame.init()

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

I = [['.....',
      '.....',
      '0000.',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....']
     ]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....'],
     ['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....']]

L = [['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....']
     ]

T = [['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....']
     ]

shapes = [S, Z, I, O, J, L, T]

colourdict = {0: (255, 255, 255),
              1: (255, 0, 0),
              2: (0, 255, 0),
              3: (0, 0, 255)}


class TetrisEnv:
    def __init__(self, height, width):
        self.positions = np.zeros((height, width))
        self.nextP = self.getRandomPiece()
        self.currP = self.getRandomPiece()
        self.currP.makeCurrent(self.positions)
        self.score = 0
        self.height = height
        self.width = width

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
            change = [0, 1]

        # up: change rotation by 1
        elif action == 'up':
            self.currP.rotation = (self.currP.rotation + 1) % len(self.currP.shape)

        # left: position in width -1
        elif action == 'left':
            change = [-1, 0]

        # right: position in width +1
        elif action == 'right':
            change = [1, 0]

        self.currP.changePosition(change[0], change[1])

        self.collDetect(change[0], change[1])

    def collDetect(self, x_changed, y_changed):
        block_positions = self.currP.get_positions()
        print(block_positions)
        collision = False

        for row in range(len(self.positions)):
            for element in range(len(self.positions[0])):
                if self.positions[row, element] != 0:
                    if (row, element) in block_positions:
                        collision = True
                        break
            if collision:
                break

        # collision detection with the game's edge
        for pos in block_positions:
            if pos[0] > len(self.positions[0]):
                self.move('left')  # Move left cause you're over right edge
            if pos[0] < 0:
                self.move('right')  # Move right cause you're over left edge
            if pos[1] <= 0:
                pass  # Reached bottom, lock block and move to the next piece
            if pos[1] > len(self.positions):
                self.endGame()

        # Als de game niet over is, check dan of er volle lijnen zijn gemaakt
        self.removeLine()

        if collision:
            self.nextBlock()

    def nextBlock(self):
        # Pak een nieuw blok klaar
        self.currP = self.nextP
        self.currP.makeCurrent(self.positions)

        self.nextP = self.getRandomPiece()

    def removeLine(self):
        full = True
        for row in range(len(self.positions)):
            for element in range(len(self.positions[0])):
                if self.positions[row, element] != 0:
                    pass
                else:
                    full = False
            if full:
                np.delete(self.positions, row, 0)
                np.insert(self.positions, 0, np.zeros((1, len(self.positions[0]))), axis=0)
            full = True

    def drawField(self):
        blocksize = 25
        edgesize = 5
        y_offset = 25
        x_offset = 25
        # Automatic scaling of displaysize:
        DISPLAYSIZE = (
            self.width * (blocksize + edgesize) + x_offset * 2 + 8 * (blocksize + edgesize),
            self.height * (blocksize + edgesize) + y_offset * 2)
        # canvas 2000x1200
        # plak erop u veld
        # rechts plak volgend stuk
        # onder rechts plak score

        display_surface = pygame.display.set_mode(size=DISPLAYSIZE)  # Set the display size

        # Draw anything inside 'positions'
        surface = pygame.Surface(DISPLAYSIZE)
        for row in range(len(self.positions)):
            for element in range(len(self.positions[0])):
                # Draw the rectangles on the Surface
                rect = pygame.Rect(
                    (element * (blocksize + edgesize) + x_offset, row * (blocksize + edgesize) + y_offset),
                    (blocksize, blocksize))
                pygame.draw.rect(surface, colourdict[self.positions[row][element]], rect)

        # TODO delete the current piece from the previous move

        # TODO draw the current piece in current rotation
        coos = self.currP.get_positions()
        for coo in range(len(coos)):
            # Draw the rectangles on the Surface
            rect = pygame.Rect(
                (coos[coo][0] * (blocksize + edgesize) + x_offset, coos[coo][1] * (blocksize + edgesize) + y_offset),
                (blocksize, blocksize))
            pygame.draw.rect(surface, (255, 0, 0), rect)

        # TODO draw the next piece in startrotation

        coos = self.nextP.get_positions()
        for coo in range(len(coos)):
            # Draw the rectangles on the Surface
            rect = pygame.Rect(
                ((coos[coo][0] + self.width + 4) * (blocksize + edgesize) + x_offset,
                 (coos[coo][1] + self.height / 8) * (blocksize + edgesize) + y_offset),
                (blocksize, blocksize))
            pygame.draw.rect(surface, (0, 255, 0), rect)

        display_surface.blit(surface, (0, 0))  # Draw the surfaces on the display
        pygame.display.flip()  # Update the display

    def endGame(self):
        # TODO endgame screen
        pass


class Piece:
    def __init__(self, shape):
        self.shape = shape

        # Position = [x,y]
        self.position = [-1, -1]
        self.rotation = 0

    def makeCurrent(self, positions):
        width = len(positions[0])
        self.position = [int(width / 2) - 1, 0]

    def get_positions(self):
        positions = []

        for i in range(len(self.shape[self.rotation])):
            for j in range(len(self.shape[self.rotation][0])):
                if self.shape[self.rotation][i][j] == '0':
                    positions.append([self.position[0] + i - 2, self.position[1] + j - 2])
        return positions

    def changePosition(self, x, y):
        self.position[0] = self.position[0] + x
        self.position[1] = self.position[1] + y
