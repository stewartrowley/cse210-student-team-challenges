class Guess:
    def __init__(self, code):
        self.code = code

    def make_hint(self, guess):
        get_hint = "****"
        for index, letter in range(enumerate((guess))):
            if self.code[index] == letter:
                get_hint += "x"
            elif letter in self.code:
                get_hint += "o"
            else:
                get_hint += "*"
        return get_hint
