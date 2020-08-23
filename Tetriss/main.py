import numpy as np
import time
from Tetriss.TetrisEnv import TetrisEnv
TetrisEnv = TetrisEnv(20, 10)
TetrisEnv.drawField()
time.sleep(5)
while True:

    TetrisEnv.move("down")
    TetrisEnv.drawField()
    time.sleep(5)