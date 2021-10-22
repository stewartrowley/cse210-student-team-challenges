import random
class Board:
    def __init__(self):
        self.guess = 0
        self.code = 0
        self._prepare()

    def _prepare(self):
        self.code = random.randint(1000, 9999)
        

    def apply(self, guess):
        self.guess = guess
        pass

    def to_string(self):
        text = "\n--------------------"
        
        text = "\n--------------------"
        pass

    def did_win(self):
        pass