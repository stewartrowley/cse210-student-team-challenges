from game.console import Console
from game.jumper import Jumper
from game.board import Board
from game.word_bank import Word_Bank

class Director:

    def __init__(self):
        
        self.console = Console()
        self.jumper = Jumper()
        self.board = Board()
        self.word_bank = Word_Bank()
        self.keep_playing = True
        self.guess = ""
        self.word = ""
        
    def start_game(self):
        self.word = self.word_bank.get_word()
        self.board.display_word(self.guess, self.word)
        self.board.display_jumper(self.jumper.wrong)
        print(" ")

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print(f"The word was {self.word}")

    def get_inputs(self):
    
        
        
        self.guess = self.console.read("Guess a letter [a-z]: ")
 
    def do_updates(self):

        
        self.jumper.check_guess(self.word, self.guess)


    def do_outputs(self):
        self.board.display_word(self.guess, self.word)
        
        self.board.display_jumper(self.jumper.wrong)
        if self.keep_playing != (self.board.check_win()):
            self.keep_playing = False
        elif self.keep_playing != (self.jumper.wrong != 4):
            self.keep_playing = False
        


    
