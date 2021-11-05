from game.point import Point
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


    # def _word(self):
        

    def _generate_word(self):
        # for word in range(5):
        while len(self._word_list) < 6:
            word = Actor()
            x = 450
            y = random.randint(1,450)
            position = Point(x, 50)
            position2 = Point(x/-100, 50)
            word.set_position(position)
            word.set_velocity(position2)
            
            word.set_text(self._words[random.randint(1,10000)])
            self._word_list.append(word)

        
            


        
    def move_word(self):
        for word in self._word_list:
            
            word.move_next()
            
        
    def _get_points(self, word):
        self._points = len(word)
        return self._points

    def _reset(self, word):
        self._word_list.remove(word)

