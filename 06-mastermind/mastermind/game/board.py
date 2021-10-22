import random
class Board:
    def __init__(self):
        self.guess = 0
        self.code = 0
        self._prepare()

    def _prepare(self):
        self.code = random.randint(1000, 9999)
        

    def apply(self, guess, hint):
        self.guess = guess
        self.hint = hint
        pass

    def to_string(self, roster):
        text = "\n--------------------"
        text += (f"{roster.self.players[0]}: {self.guess}, {self.hint}")
        text += (f"{roster.self.players[1]}: {self.guess}, {self.hint}")
        text += "\n--------------------"
        return text

    def did_win(self):
        if self.guess == self.code:
            return True
        