from game.word import Word
from game.actor import Actor
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        
        self._buffer = ""
        position = Point(30, 10)
        self.set_position(position)
        self.set_text(f"Buffer: {self._buffer}")

    def _check_word(self, word):

        input_list = []
        
        while word == self._buffer:
            input_list.append(self.set_text())
            return input_list
        


            

        




