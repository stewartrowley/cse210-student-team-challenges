import os

FRAME_RATE = 30

MAX_X = 500
MAX_Y = 500

FRAME_LENGTH = 5

STARTING_WORDS = 5

DEFAULT_SQUARE_LENGTH = 20
DEFAULT_FONT_SIZE = 16
DEFAULT_TEXT_OFFSET = 5

PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
