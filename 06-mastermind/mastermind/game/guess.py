class Guess:
    def __init__(self, code):
        
        self.code = []
        for number in str(code):
            self.code.append(int(number))


    def make_hint(self, guess):
        get_hint = ""
        get_guess = []
        for number in str(guess):
            get_guess.append(int(number))
 
        for index, letter in enumerate(get_guess):
            if self.code[index] == letter:
                get_hint += "x"
            elif letter in self.code:
                get_hint += "o"
            else:
                get_hint += "*"
        return get_hint
