from game.actor import Actor
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
        self._points = 0


    def _word(self):
        for i in self._words(range(5)):
            self._words.append(self._word_list[i])

    def _generate_word(self):

        for i in self._word_list:
            Actor.set_velocity(0, -1)

        pass
        
    def _get_points(self, word):
        self._points = len(word)
        return self._points

    def _reset(self, word):
        self._word_list.remove(word)

