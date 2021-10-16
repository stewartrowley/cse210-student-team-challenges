class Board:
    def __init__(self):
        
        self.display = []
        self.start = 0
    
        
    def display_word(self, guess, word):
        
        while self.start == 0:
            for i in range(len(word)):
                self.display.append('_')
            self.start += 1
        
        
        for position in range(len(word)):
            letter = word[position]
            if guess == letter:
                self.display[position] = letter
        for i in self.display:
            print(i, end=" ")
    def check_win(self):
        
        if self.display.count('_') == 0:
            print('You win!')
            return False
        else: 
            return True



    def display_jumper(self, wrong):
        print(' ')
        if wrong == 0:
            print(' ')
            print(' ' + ' ' + '___')
            print(' /' + '___' + '\\')
            print(' ' + '\\' + '   ' + '/')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong == 1:
            print(' ')
            print(' /' + '___' + '\\')
            print(' ' + '\\' + '   ' + '/')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong == 2:
            print(' ')
            print(' ' + '\\' + '   ' + '/')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong == 3:
            print(' ')
            print('  ' + '\\' + ' ' + '/')
            print('   0')
            print('  /|\\')
            print('  /' + ' ' + '\\')
        elif wrong == 4:
            print(' ')
            print('   x')
            print('  /|\\')
            print('  /' + ' ' + '\\')



