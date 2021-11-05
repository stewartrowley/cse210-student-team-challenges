import random
from game import constants
from game.actor import Actor

class Word(Actor):

    def __init__(self):
        super().__init__()
        self._word_list = []
        self._words = constants.LIBRARY
        self._height = constants.DEFAULT_SQUARE_LENGTH
        self._width  = constants.DEFAULT_SQUARE_LENGTH

    def _word(self):
        for i in self._words:
            self._words.append[i]
        

        
        
    def _get_points(self):
        return 

    def _reset(self):
        pass


