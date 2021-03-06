import numpy as np
from skimage.color import rgb2gray
from skimage.transform import resize
import pickle


def preprocess(frame):
    frame = frame[35:195, :]
    frame = rgb2gray(frame)*255
    frame = resize(frame, (84, 84))
    return frame.astype(np.uint8)


def save_to_file(some_list):
    with open('training_data.data', 'wb') as fp:
        pickle.dump(some_list, fp)
        print('Training data dumped to pickle.')

def choose_game(game_name):
    if game_name == 'PONG':
        return 'PongDeterministic-v4'
    elif game_name == 'BREAKOUT':
        return 'BreakoutDeterministic-v4'
    else:
        raise ValueError('An invalid game name chosen!')