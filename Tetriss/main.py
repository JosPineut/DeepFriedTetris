import numpy as np
import time

import pygame

from Tetriss.TetrisEnv import TetrisEnv

TetrisEnv = TetrisEnv(20, 10)
TetrisEnv.drawField()
time.sleep(0.1)
start = time.time()
alive = True

while alive:
    TetrisEnv.drawField()
    stop = time.time()
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
                start = time.time()
    if stop-start >= TetrisEnv.fall_time:
        TetrisEnv.move("down")
        start = time.time()
    alive = not TetrisEnv.done
pygame.quit()




