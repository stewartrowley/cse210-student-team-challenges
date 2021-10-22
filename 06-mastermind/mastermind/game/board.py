import random
class Board:
    def __init__(self):
        self.guess = 0
        self.guess1 = '----'
        self.guess2 = '----'
        self.code = 0
        self.hint = ""
        self.hint1 = "****"
        self.hint2 = "****"
        self._prepare()
        self.x = 0

    def _prepare(self):
        self.code = random.randint(1000, 9999)
        

    def apply(self, guess, hint):
        self.guess = guess
        self.hint = hint
        
        
        while self.x < 10:
            if self.x % 2 == 0:
                self.guess1 = guess
                self.hint1 = hint
                break
            
            else:
                self.guess2 = guess
                self.hint2 = hint
                break
        self.x += 1        


    def to_string(self, roster):
        text = "\n--------------------"
        text += (f"\n{roster.players[0]._name}: {self.guess2}, {self.hint2}")
        text += (f"\n{roster.players[1]._name}: {self.guess1}, {self.hint1}")
        text += "\n--------------------"
        return text

    def did_win(self):
        if self.guess == self.code:
            return True
        