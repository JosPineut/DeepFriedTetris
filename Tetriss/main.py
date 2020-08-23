import numpy as np
import time

import pygame

from Tetriss.TetrisEnv import TetrisEnv

TetrisEnv = TetrisEnv(20, 10)
TetrisEnv.drawField()
time.sleep(0.1)

getal = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                TetrisEnv.move("left")
            elif event.key == pygame.K_RIGHT:
                TetrisEnv.move("right")
            elif event.key == pygame.K_UP:
                TetrisEnv.move("up")
            elif event.key == pygame.K_DOWN:
                TetrisEnv.move("down")

    TetrisEnv.drawField()
    #time.sleep(0.4)