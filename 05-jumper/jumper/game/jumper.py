
class Jumper:

    def __init__(self):
        self.guess = ['a']
        self.wrong = 0

    def check_guess(self, word, guess):
        self.guess.append(guess)
        
        if word.find(self.guess[-1]) != -1:
            self.wrong += 0
        else:
            self.wrong += 1

        return self.wrong
            


