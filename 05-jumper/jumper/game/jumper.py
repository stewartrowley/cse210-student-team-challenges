
class Jumper:

    def __init__(self):
        self.guess = []

    def check_guess(self, word):
        correct = False
        for element in word:
            if self.guess[-1] == element:
                correct = True
        for element in self.guess:
            if self.guess[-1] == element:
                correct = False
        return correct
            


