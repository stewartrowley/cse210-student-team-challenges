
class Jumper:

    def __init__(self):
        self.guess = []
        self.wrong = 0

    def check_guess(self, word):
        
        for element in word:
            if self.guess[-1] == element:
                self.wrong += 0
        
            elif self.guess[-1] != element:
                
                self.wrong += 1
        return self.wrong
            


