import numpy as np

from Tetriss.TetrisEnv import TetrisEnv
positions = np.zeros((10, 20))

for row in range(len(positions)):
    for element in range(len(positions[0])):
        if(positions[row, element]) != 0:
            print("0")