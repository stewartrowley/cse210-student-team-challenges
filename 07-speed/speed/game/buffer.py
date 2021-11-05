from game.word import Word
from game.actor import Actor
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        
        super().__init__()
        self._buffer = ""
        position = Point(10, 475)
        self.set_position(position)
        self.set_text(f"Buffer: {self._buffer}")

    def do_input(self):
        
        self._buffer = 
        self.set_text(f"Buffer: {self._buffer}")

    def _check_word(self, word):

        if word == self._buffer:
            return True
        else:
            return False    

