class Board:
    def __init__(self):
        self.word = ''
        self.display = []

    def display_word(self, guess):
        letter = []
        for letter in len(self.word):
            self.display.append('_')
            print(self.display)
        for position in range(len(self.word)):
            letter = self.word[position]
            if guess == letter:
                self.display[position] = letter
                print(self.display)

    def display_jumper(self, wrong):
        if wrong == 0:
            print(' ' + ' ' + '___')
            print(' /' + '___' + '\\')
            print(' ' + '\\' + '   ' + '/')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong >= 1:
            print(' /' + '___' + '\\')
            print(' ' + '\\' + '   ' + '/')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong >= 2:
            print(' ' + '\\' + '   ' + '/')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong >= 3:
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong >= 4:
            print('   x')
            print('  /|\\')
            print('  /' + ' ' + '\\')



