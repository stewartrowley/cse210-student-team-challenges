import os

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 0.08
STARTING_WORDS = 5
DEFAULT_SQUARE_LENGTH = 20
DEFAULT_FONT_SIZE = 16
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
