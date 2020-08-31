import time
import pygame
from Tetriss.TetrisEnv import TetrisEnv
import pickle
import numpy as np

# gebruikte sourcecode: https://pythonprogramming.net/own-environment-q-learning-reinforcement-learning-python-tutorial/
HEIGHT = 20
WIDTH = 10

HM_EPISODES = 25000
LINE_REWARD = 25  #
epsilon = 0.5  # randomness
EPS_DECAY = 0.9999  # Every episode will be epsilon*EPS_DECAY
SHOW_EVERY = 1000  # how often to play through env visually.

start_q_table = None  # if we have a pickled Q table, we'll put the filename of it here.

LEARNING_RATE = 0.1
DISCOUNT = 0.95

actions = ['up', 'down', 'right', 'left']

if start_q_table is None:
    # initialize the q-table
    pass
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

# Start training
episode_rewards = []
for episode in range(HM_EPISODES):
    # Initialize game
    TetrisEnv = TetrisEnv(HEIGHT, WIDTH)
    TetrisEnv.drawField()
    start = time.time()
    alive = True

    # Logic to visualise or not
    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True
    else:
        show = False

    episode_reward = 0
    for i in range(1000):  # Max aantal steps
        obs = 0
        # obs = # TODO position of each block in the positions + currP (+ nextP?)
        # print(obs)
        if np.random.random() > epsilon:
            # GET THE ACTION
            action = np.argmax(q_table[obs])
        else:
            action = np.random.choice(actions)
        # Take the action!
        TetrisEnv.move(action)

        # Handling the rewarding
        # TODO rewarding in means of removed lines or penalty when creating holes in screen

        # Update Q-table
        new_obs = 0  # TODO new positions of each block
